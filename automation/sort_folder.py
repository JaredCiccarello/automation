import os
import shutil

def sort_documents(folder_path):
    root_directory = os.path.dirname(folder_path)

    logs_folder = os.path.join(root_directory, "logs")
    mail_folder = os.path.join(root_directory, "mail")
    os.makedirs(logs_folder, exist_ok=True)
    os.makedirs(mail_folder, exist_ok=True)

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1]
            if file_extension == '.txt':
                shutil.move(file_path, os.path.join(logs_folder, file))
                print(f"Moved {file} to logs folder")
            elif file_extension == '.mail':
                shutil.move(file_path, os.path.join(mail_folder, file))
                print(f"Moved {file} to mail folder")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ")
    if os.path.exists(folder_path):
        sort_documents(folder_path)
    else:
        print(f"Folder {folder_path} does not exist!")


