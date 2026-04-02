import os

def load_codebase(folder_path):
    code_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".py", ".java", ".js")):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        code_data.append({
                            "file_name": file,
                            "file_path": file_path,
                            "content": content
                        })

                except Exception as e:
                    print(f"Error reading {file}: {e}")

    return code_data