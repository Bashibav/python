import os

# Specify the directory (you can change this to any path you want)
directory_path = '/Program Files'  # '.' means current directory

# using module to list the directories
contents=os.listdir(directory_path)

# printing the directories
print(contents)