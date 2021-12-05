# External imports
import sys


def read_file(path: str) -> str:
    """Reads a file and returns the content as a string (no strip)

    :param path:    The file to read
    :type path:     str

    :return:    The content of the file
    :rtype:     str
    """
    with open(path, 'r') as file:
        data = file.read()
        return (data)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    try:
        result = read_file(sys.argv[1])
        print(result)
    except (IOError, OSError) as err:
        print(f'An error occured: {err}', file=sys.stderr)
