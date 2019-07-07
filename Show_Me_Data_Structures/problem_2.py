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
    result = []

    def find_dir(directory):
        for f in os.listdir(directory):
            full_path = join(directory, f)

            if isdir(full_path):
                find_dir(full_path)
            else:
                if f.endswith(suffix):
                  result.append(full_path)

    find_dir(path)

    return sorted(result)

print (find_files(".c", "testdir")) # Return all directories 
