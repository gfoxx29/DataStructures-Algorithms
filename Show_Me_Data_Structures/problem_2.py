## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os
from os.path import isdir, dirname, join

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    list_of_paths = []
    
    def search_dir(directory):
        try:
            for files in os.listdir(directory):
                dirpath = join(directory, files)
                if isdir(dirpath):
                    search_dir(dirpath)
                elif files.endswith(suffix):
                    list_of_paths.append(dirpath)
        except FileNotFoundError:
            print("This path doesn't exist!")

    search_dir(path)
    if not list_of_paths:
        print("No file found!")

    return list_of_paths

# Test cases
print(find_files(".c", "testdir"))  # Return all directories 
print(find_files(".c", "datadir"))  # Print "This path doesn't exist!" 
print(find_files(".py", "testdir")) # Print "No file found!" 
