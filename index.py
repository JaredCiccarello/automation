from rich.console import Console
from rich.prompt import Prompt
import os
import sys
from automation.create_folder import create_folder
from automation.temp_folder import move_user_documents
from automation.sort_folder import sort_documents
from automation.parse_file import parse_log_file
from automation.count import count_files_by_extension

def main():
    console = Console()
    while True:
        console.print(
            "\n1. Create a folder\n2. Delete a user\n3. Sort Documents\n4. Parse a log file\n5. Specific file-type amount\n(q) Quit",
            style="bold blue"
        )
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "q"], default="q")

        if choice == "1":
            folder_name = Prompt.ask("Enter folder name")
            create_folder(folder_name)

        elif choice == "2":
            folder = Prompt.ask("Enter folder name")
            file = Prompt.ask("Enter file name")
            if os.path.exists(f"{folder}/{file}"):
                move_user_documents(folder, file)
                console.print(f"File '{file}' moved to temp folder!", style="bold green")
            else:
                console.print("Either folder or file does not exist!", style="bold red")

        elif choice == "3":
            folder_path = Prompt.ask("Enter folder path")
            if os.path.exists(folder_path):
                sort_documents(folder_path)
            else:
                console.print(f"Folder {folder_path} does not exist!", style="bold red")

        elif choice == "4":
            log_file_path = Prompt.ask("Enter log file path")
            if os.path.exists(log_file_path):
                parse_log_file(log_file_path, "logs")
            else:
                console.print("Log file does not exist!", style="bold red")

        elif choice == "5":
            file_extension = input("Enter file extension: ")
            folder_path = input("Enter folder path: ")
            if os.path.exists(folder_path):
                count = count_files_by_extension(file_extension, folder_path)
                console.print(f"Number of {file_extension} files in {folder_path} is {count}", style="bold green")
            else:
                console.print(f"Folder {folder_path} does not exist!", style="bold red")


        elif choice.lower() in ["q", "quit"]:
            do_exit("Exiting...")
        else:
            console.print("Invalid choice. Try again.", style="bold red")

def do_exit(message):
    sys.exit(message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        do_exit("Ctrl+C detected! Exiting...")
