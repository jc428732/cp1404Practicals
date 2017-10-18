import os
import shutil
os.chdir("FilesToSort")

existing_file_types = {}
for filename in os.listdir("."):
    if filename.split(".")[1] not in existing_file_types.keys():
        category = input("What category would you like to sort {} files into?\n".format(filename.split(".")[1]))
        existing_file_types[filename.split(".")[1]] = category
        if category not in existing_file_types.values():
            os.mkdir(category)
    shutil.move(filename, existing_file_types[filename.split(".")[1]])