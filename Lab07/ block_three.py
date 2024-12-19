import os
import shutil

def rename_file_or_folder():
    path = input("Enter the path of the file/folder to rename: ").strip()
    new_name = input("Enter the new name: ").strip()
    if not os.path.exists(path):
        print("Error: The specified path does not exist.")
        return

    new_path = os.path.join(os.path.dirname(path), new_name)
    try:
        os.rename(path, new_path)
        print(f"Successfully renamed to: {new_path}")
    except Exception as e:
        print(f"Error: {e}")

def copy_file_or_folder():
    source_path = input("Enter the path of the file/folder to copy: ").strip()
    destination_path = input("Enter the destination path: ").strip()
    if not os.path.exists(source_path):
        print("Error: The source path does not exist.")
        return

    if os.path.exists(destination_path):
        print("Error: The destination path already exists.")
        return

    try:
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
        else:
            shutil.copytree(source_path, destination_path)
        print(f"Successfully copied to: {destination_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nFile Manager Options:")
        print("7 - Rename file/folder")
        print("8 - Copy file/folder")
        print("0 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '7':
            try:
                rename_file_or_folder()
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == '8':
            try:
                copy_file_or_folder()
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == '0':
            print("Exiting the File Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if name == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical error: {e}")