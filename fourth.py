import os

def find_file():
    folder_path = "C:\Users\mft\Desktop\AliAgha.project"  
    file_name = input("Enter the file name: ")

    for file in os.listdir(folder_path):
        if file == file_name:
            print(f"File found: {os.path.join(folder_path, file)}")
            return

    print("File not found.")

find_file()