import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    file_root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(file_root_path)
    abs_path = os.path.abspath(os.path.join(root_path, working_directory, file_path))

    if not abs_path.startswith(os.path.join(root_path, working_directory)):
        print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        return
    
    if not os.path.exists(abs_path):
        print(f'Error: File "{file_path}" not found.')
        return

    if not abs_path.endswith(".py"):
        print(f'Error: "{file_path}" is not a Python file.')
        return

    try:
        result = subprocess.run(
            ["python3", abs_path] + args,
            capture_output=True,
            text=True,
            timeout=30
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if result.stdout == "" and result.stderr == "":
        return "No output produced."
    
    if result.returncode == 0:
        return_string = f"""
        STDOUT: {result.stdout}
        STDERR: {result.stderr}
        Process exited with code {result.returncode}
        """
    else:
        return_string = f"""
        STDOUT: {result.stdout}
        STDERR: {result.stderr}
        """
    print(return_string)
    return return_string

if __name__ == "__main__":
    run_python_file("calculator", "main.py")