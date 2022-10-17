import os
import shutil
import send2trash

f = open("practice.txt", "w+")
f.write("Hello there")
f.close()

print(os.getcwd())  # get current working directory
print(os.listdir("/Users"))  # list directory

# moving a file
# shutil.move("practice.txt", "/Users/mrtn")
print(os.listdir("/Users/mrtn"))  # list directory

# send2trash.send2trash("/Users/mrtn/practice.txt")

for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f"Currently looking at: {folder} \n ")
    print("Subfolders are: ")
    for sub_folder in sub_folders:
        print(f"\tSubfolder: {sub_folder}")
    print("\nThe files are: ")
    for f in files:
        print(f"\tFile: {f}")