import os
import re
import shutil

def replace_in_md_files():
    secret_block = re.compile(r'```secret.*?```', re.DOTALL)
    secret_line = re.compile(r'`.*?`')
    secret_link = re.compile(r'\!?\[\[(?:.*\/)*_.*?\]\]')

    for root, dirs, files in os.walk("./content"):
        for dir in dirs:
            if dir.startswith("_"):
                shutil.rmtree(os.path.join(root, dir))
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                if file.startswith("_"):
                    os.remove(file_path)
                    continue

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = secret_link.sub("", secret_line.sub("", secret_block.sub("", content)))

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

replace_in_md_files()

