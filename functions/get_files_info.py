import os
def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_directory = os.path.abspath(working_directory)

    if not abs_path.startswith(abs_working_directory):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    if not os.path.isdir(abs_path):
        print(f'Error: "{abs_path}" is not a directory')
        return
    
    contents_of_directory = os.listdir(abs_path)
    print(f"Result for {directory} directory:")
    for file in contents_of_directory:
        file_path = os.path.join(abs_path, file)
        is_dir = os.path.isdir(file_path)
        file_size = os.path.getsize(file_path)
        print(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
