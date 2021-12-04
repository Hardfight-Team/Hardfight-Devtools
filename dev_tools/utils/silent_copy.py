# External imports
import contextlib
import shutil
import sys
import os


def silent_copy(src: str, dest: str):
    """Silent copies a directory or a file

    :param src:     Source directory or file
    :type src:        str
    :param dest:    Destination file or directory name
    :type dest:     str
    """
    with contextlib.suppress(FileExistsError, FileNotFoundError):
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copyfile(src, dest)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <src> <dest>', file=sys.stderr)
        sys.exit(1)
    silent_copy(sys.argv[1], sys.argv[2])
