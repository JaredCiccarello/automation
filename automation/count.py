from rich.console import Console
import os

console = Console()

def count_files_by_extension(file_extension, folder_path):
    files = os.listdir(folder_path)
    count = 0
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and os.path.splitext(file)[1] == file_extension:
            count += 1
    return count

if __name__ == "__main__":
    file_extension = input("Enter file extension: ")
    folder_path = input("Enter folder path: ")
    if os.path.exists(folder_path):
        count = count_files_by_extension(file_extension, folder_path)
        console.print(f"Number of {file_extension} files in {folder_path} is {count}", style="bold green")
    else:
        console.print(f"Folder {folder_path} does not exist!", style="bold red")
