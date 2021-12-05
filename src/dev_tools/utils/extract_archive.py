# External imports
import zipfile
import sys
import os


class ZipFileWithPermissions(zipfile.ZipFile):
    """Custom ZipFile class handling file permissions"""
    def _extract_member(self, member, targetpath, pwd):
        if not isinstance(member, zipfile.ZipInfo):
            member = self.getinfo(member)
        targetpath = super()._extract_member(member, targetpath, pwd)
        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(targetpath, attr)
        return (targetpath)


def extract_archive(zip_file: str, dest: str):
    """Extracts ZIP file into a given destination

    :param zip_file:    ZIP file
    :type zip_file:     str
    :param dest:        Destination file
    :type dest:         str
    """
    with ZipFileWithPermissions(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <src> <dest>', file=sys.stderr)
        sys.exit(1)
    extract_archive(sys.argv[1], sys.argv[2])
