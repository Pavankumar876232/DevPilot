from app.code_parser import load_codebase

data = load_codebase("data/sample_repo")

for file in data:
    print("File:", file["file_name"])
    print("Content:", file["content"])
    print("-" * 40)