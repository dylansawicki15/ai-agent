import os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    file_root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(file_root_path)
    abs_path = os.path.abspath(os.path.join(root_path, working_directory, file_path))

    if not abs_path.startswith(os.path.join(root_path, working_directory)):
        print(f'Error: Cannot read "{abs_path}" as it is outside the permitted working directory')
        return
    
    if not os.path.isfile(abs_path):
        print(f'Error: File not found or is not a regular file: "{abs_path}"')
        return


    print(f"Reading file: {abs_path}")
    with open(abs_path, 'r') as file:
        file_content_string = file.read()
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS]
            file_content_string += f'[...File "{abs_path}" truncated at 10000 characters]'
        print(file_content_string)
        return file_content_string