from rich.console import Console
import os
import shutil

console = Console()

def move_user_documents(folder, file):
    os.makedirs("temp", exist_ok=True)
    shutil.move(os.path.join(folder, file), "temp")

if __name__ == "__main__":
    folder = input("Enter folder name: ")
    file = input("Enter file name: ")
    file_path = os.path.join(folder, file)
    if os.path.exists(file_path):
        move_user_documents(folder, file)
        console.print(f"File '{file}' moved to temp folder!", style="bold green")
    else:
        console.print(f"Either folder or file does not exist!", style="bold red")