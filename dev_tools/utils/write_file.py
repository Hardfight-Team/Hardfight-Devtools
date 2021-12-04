# External imports
import sys


def write_file(path: str, content: str):
    """Writes the given content into a file

    :param path:        The file to write on
    :type path:         str
    :param content: The content to wirte
    :type path:         str
    """
    with open(path, 'w+') as file:
        file.write(content)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <path> <content>', file=sys.stderr)
        sys.exit(1)
    try:
        write_file(sys.argv[1], sys.argv[2])
    except (IOError, OSError) as err:
        print(f'An error occured: {err}', file=sys.stderr)
