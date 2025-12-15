import os
# Spicify the directory you want to list
directory_path = os.path.dirname(os.path.abspath(__file__))
# List all files in the specified directory
files = os.listdir(directory_path)
for file in files:
    print(file)