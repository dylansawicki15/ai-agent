from get_file_content import get_file_content
from get_files_info import get_files_info
from write_file import write_file
from run_python import run_python_file

if __name__ == "__main__":
    run_python_file("calculator", "main.py") 
    run_python_file("calculator", "main.py", ["3 + 5"])
    run_python_file("calculator", "tests.py")
    run_python_file("calculator", "../main.py")
    run_python_file("calculator", "nonexistent.py")