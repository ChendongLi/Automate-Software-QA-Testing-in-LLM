import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"  # match your deployment's API version
)

QA_TEST_INSTRUCTION_PROMPT = """
You are a helpful assistant that detect the root cause of the bug in the code.
You will be given a code repository that contains all the code of the project.
You will also be given a log that contains the error message and stack trace of the bug
You will analyze the code and the log, and then you will give a detailed answer about the root cause of the bug:
- the bug is located in the code
- what is the bug
- how to fix it.

Full code repository:
```python
{full_code}
"""


def ask_azure_openai(full_code: str, log: str) -> str:
    messages = [
        {"role": "system", "content": QA_TEST_INSTRUCTION_PROMPT.format(full_code=full_code)},
        {"role": "user", "content": log}
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # replace with your deployment name
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"