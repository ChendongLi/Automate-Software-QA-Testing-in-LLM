import os
def collect_code_files(repo_path: str) -> str:
    code_blocks = []
    for root, dirs, files in os.walk(repo_path):
        # Skip the llm folder
        if "llm" in dirs:
            dirs.remove("llm")

        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_path)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    code_blocks.append(f"# File: {rel_path}\n```\n{content}\n```")
    return "\n\n".join(code_blocks)

if __name__ == "__main__":
    repo_path = os.path.dirname("/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/example/fastapi-sample")
    code_snippets = collect_code_files(repo_path)
    print(code_snippets)