# External imports
from typing import List
import fnmatch
import sys
import os


def find_paths(root: str, pattern: str) -> List[str]:
    """Find paths in subdirectories of files matching the pattern

    :param root:        Root directory to look for files
    :type root:         str
    :param pattern: Pattern matching the file names
    :type pattern:    str
    """
    found_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        all_paths = filenames + dirnames
        for path in all_paths:
            if fnmatch.fnmatch(path, pattern):
                full_path = os.path.join(dirpath, path)
                found_files.append(full_path)
    return (found_files)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <root> <pattern>', file=sys.stderr)
        sys.exit(1)
    files_found = find_paths(sys.argv[1], sys.argv[2])
    for file in files_found:
        print(file)
