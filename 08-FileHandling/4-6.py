def file_stats(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        num_lines = content.count('\n')+1
        num_characters = len(content)
        num_words = len(content.split())

        print(f"File name: {file_name}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")
    except FileNotFoundError:
         print(f"Error: The file '{file_name}' does not exist. Please check the filename and try again.")

file_name=input("Enter the name of the file: ")
file_stats(file_name)
