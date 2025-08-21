from get_files_info import get_files_info

if __name__ == "__main__":
    get_files_info("../calculator", ".")
    get_files_info("../calculator", "pkg")
    get_files_info("../calculator", "/bin")
    get_files_info("../calculator", "../")