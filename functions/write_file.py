import os

def write_file(working_directory, file_path, content):
    file_root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(file_root_path)
    abs_path = os.path.abspath(os.path.join(root_path, working_directory, file_path))

    if not abs_path.startswith(os.path.join(root_path, working_directory)):
        print(f'Error: Cannot write to "{abs_path}" as it is outside the permitted working directory')
        return
    # if file does not exist, create it
    if not os.path.exists(abs_path):
        with open(abs_path, 'w') as file:
            file.write(content)
    # if file exists, overwrite it
    else:
        with open(abs_path, 'w') as file:
            file.write(content)
    print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')