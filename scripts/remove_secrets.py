import os
import re

def replace_in_md_files():
    secret_block = re.compile(r'your_regex_pattern_here')
    secret_line = re.compile(r'your_regex_pattern_here')
    secret_link = re.compile(r'your_regex_pattern_here')

    for root, _, files in os.walk("./content"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                if file.startswith("_"):
                    os.remove(file_path)
                    continue

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = secret_line.sub("", secret_block.sub("", content))

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

replace_in_md_files()
