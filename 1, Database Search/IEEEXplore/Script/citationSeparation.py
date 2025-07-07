import os
import re

def fix_bracket_ending(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.bib'):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                # Strip the newline for easier pattern matching
                stripped_line = line.rstrip('\n')
                
                # If the line ends with ",}" plus optional whitespace, do the transformation
                if re.search(r',}\s*$', stripped_line):
                    # Remove ",}" and any trailing spaces
                    content = re.sub(r',}\s*$', '', stripped_line)
                    # Write the content as one line
                    new_lines.append(content + "\n")
                    # Then write "}" on its own line
                    new_lines.append("}\n")
                else:
                    # Leave the line as-is
                    new_lines.append(line)

            # Overwrite the file with the new content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

    print("Done! Each ',}' is now split into two lines.")

if __name__ == '__main__':
    folder_path = r"C:\Users\David\Documents\Skole\A Master\Search String 1 results\IEEEXplore\Bibtex files"
    fix_bracket_ending(folder_path)
