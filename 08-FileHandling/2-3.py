###
# Makes a copy of a text file
#

# file names
original_file = r"C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\healthy_lifestyle.txt"
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as source_file:
    content = source_file.read()

# write the content to the target file (copy)
with open(target_file, 'w') as destination_file:
    destination_file.write(content)

print(f"Contents of {original_file} have been copied to {target_file}.")
