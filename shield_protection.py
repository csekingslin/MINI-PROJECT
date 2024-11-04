import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
# virus signatures 
virus_signatures = [
    rb"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
]

def scan_file(file_path):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            for signature in virus_signatures:
                if signature in file_content:
                    print(f"Virus found in file: {file_path}")
                    return
            print(f"No virus found in file: {file_path}")
    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")

def scan_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            scan_file(file_path)

def file_open():
    Tk().withdraw()  # its what is that . Hide the root window
    choice = input("Enter 'f' to scan a file or 'd' to scan a directory: ").strip().lower()
    
    if choice == 'f':
        file_path = askopenfilename()  # Open file dialog
        if file_path:
            scan_file(file_path)
        else:
            print("No file selected.")
    elif choice == 'd':
        directory_path = askdirectory()  # Open directory dialogp
        if directory_path:
            scan_directory(directory_path)
        else:
            print("No directory selected.")
    else:
        print("Invalid choice. Please enter 'f' or 'd'.")

if __name__ == "__main__":
    file_open()