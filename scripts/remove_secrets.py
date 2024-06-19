import os
import re

def replace_in_md_files():
    secret_block = re.compile(r'```secret.*?```', re.DOTALL)
    secret_line = re.compile(r'`.*?`')
    secret_link = re.compile(r'\!?\[\[_.*?\]\]')

    for root, _, files in os.walk("./content"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(file_path)
                
                if file.startswith("_"):
                    os.remove(file_path)
                    continue

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = secret_link.sub("", secret_line.sub("", secret_block.sub("", content)))

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

replace_in_md_files()

