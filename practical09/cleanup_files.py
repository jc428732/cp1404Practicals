"""
CP1404/CP5632 Practical
File renaming and os examples
"""

import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Lyrics')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for dir_name, dirs, files in os.walk("."):
        for filename in files:
        # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)

            # Option 1: rename file to new name - in place
                try:
                    os.rename("{}/{}".format(dir_name, filename), "{}/{}".format(dir_name, new_name))
                except FileExistsError:
                    pass
                except FileNotFoundError:
                    pass

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            #os.chdir('..')  # .. means "up" one directory
            #for dir_name, subdir_list, file_list in os.walk('.'):
                #print("In", dir_name)
                #print("\tcontains subdirectories:", subdir_list)
                #print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = []
    previous_character = ""
    for character in filename:
        if character.isupper() & previous_character.isalnum():
            new_name.append("_")
        new_name.append(character)
        previous_character = character

    return "".join(new_name).title().replace(".Txt", ".txt")


main()
