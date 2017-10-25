import os
import shutil
os.chdir("FilesToSort/FilesToSort")

existing_file_types = {}
for filename in os.listdir("."):
    print(filename)
    if not filename.split(".")[1] in existing_file_types:
        category = input("What category would you like to sort {} files into?\n".format(filename.split(".")[1]))
        if category not in existing_file_types.values():
            os.mkdir(category)
        existing_file_types[filename.split(".")[1]] = category
    shutil.move(filename, existing_file_types[filename.split(".")[1]])