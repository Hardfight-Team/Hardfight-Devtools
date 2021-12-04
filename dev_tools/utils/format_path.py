# External imports
import sys
import os


def format_path(path: str) -> str:
    """Gets path formatted for the current OS

    :param path:    Path with '/' as separator
    :type path:     str

    :return:    OS formatted path
    :rtype:     str
    """
    new_path = os.path.join(*path.split('/'))
    if sys.platform == 'win32':
        # Patches simple backslashes in Windows
        new_path = new_path.replace('\\', '\\\\')
    return (path)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    formatted_path = format_path(sys.argv[1])
    print(formatted_path)
