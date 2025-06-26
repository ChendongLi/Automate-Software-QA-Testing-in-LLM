import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env if exists
print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(instruction: str, user_question: str) -> str:
    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": user_question}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
