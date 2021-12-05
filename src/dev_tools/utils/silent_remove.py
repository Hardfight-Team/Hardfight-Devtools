# External imports
import contextlib
import shutil
import sys
import os


def silent_remove(path: str):
    """Silent removes a directory or a file

    :param path:    Path to remove
    :type path:     str
    """
    with contextlib.suppress(FileNotFoundError):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    silent_remove(sys.argv[1])
