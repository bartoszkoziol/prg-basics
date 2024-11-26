import re

try:
    with open(r"C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\files.txt", 'r') as file:
        file_names = file.readlines()

    pattern = r".+\.\w{4}$"

    print("File name with 4-char extension: ")

    for file_name in file_names:
        if re.match(pattern, file_name):
            print(file_name)
except FileNotFoundError:
      print("The file 'files.txt' does not exist. Please ensure it is in the same directory as this script.")