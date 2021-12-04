# External imports
import shutil
import sys
import os


def make_archive(src: str, dest: str):
    """Make an archive with the given source

    :param src:     Source directory (to archive)
    :type src:      str
    :param dest:    Archive destination
    :type dest:     str
    """
    base = os.path.basename(dest).split('.')
    name = base[0]
    format = base[1]
    archive_from = os.path.dirname(src)
    archive_to = os.path.basename(src.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), dest)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <src> <dest>', file=sys.stderr)
        sys.exit(1)
    make_archive(sys.argv[1], sys.argv[2])
