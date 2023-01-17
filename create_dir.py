import os
import time
import sys
from colors import Colors

CURRENT_DIR = f"{os.getcwd()}/"
FOLDERS_NAME = []
PROGRAM_NAME = "create_dir.py"

ARGS_EXPLANATION = {
    "<directory_name>": "The name of the root directory that will be created. Cannot containt .txt extension!",
    "<file.txt>": "the file from where the sub directories names are takend and created, <file.txt> must containt .txt extension!",
}


def help():
    print(f"{Colors.FAIL}Usage: python3 {PROGRAM_NAME} <directory name> <file.txt>")
    print(
        f"{Colors.WARNING}EXAMPLE USAGE: python3 {PROGRAM_NAME} Programming directories.txt"
    )
    for key, value in ARGS_EXPLANATION.items():
        print(f"{Colors.OKGREEN}{key} | {value}")


def check_if_right_arg():
    if sys.argv[1].lower().endswith(".txt") or not sys.argv[2].lower().endswith(".txt"):
        sys.exit(help())


def store_from_txt_to_list(file):
    try:
        with open(file, "r", encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                FOLDERS_NAME.append(line.strip())
        return FOLDERS_NAME
    except FileNotFoundError:
        sys.exit(
            f"{Colors.FAIL}File {file} not found!\nPlease make sure you have .txt file with the folders name!"
        )


def create_folder(root_dir, subfolders):
    folder_name = sys.argv[1].strip()  # Free choice of name for the root directory
    main_dir = os.path.join(CURRENT_DIR, folder_name)
    FOLDERS_NAME = store_from_txt_to_list(sys.argv[2])
    try:
        os.mkdir(main_dir)
    except OSError as error:
        print(f"{Colors.FAIL}{error}")
        sys.exit(1)
    time.sleep(1)
    try:
        os.chdir(main_dir)
    except OSError as error:
        print(f"{Colors.FAIL}{error}")
        sys.exit(1)

    try:
        for item in FOLDERS_NAME:
            os.mkdir(item)
    except OSError as error:
        print(f"{Colors.FAIL}{error}")
        sys.exit(1)
    print(f"{Colors.OKGREEN}Directories created successfully!")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "help".lower().strip():
        sys.exit(help())

    elif len(sys.argv) != 3:
        sys.exit(
            f"{Colors.FAIL}Usage: python3 {PROGRAM_NAME} <directory name> <file.txt>\n'run python3 {PROGRAM_NAME} help' for more info"
        )

    check_if_right_arg()
    create_folder(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
