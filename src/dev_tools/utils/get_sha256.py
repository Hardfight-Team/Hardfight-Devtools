# External imports
import checksumdir    # type: ignore
import hashlib
import sys
import os


# Read file chunck size
HASH_CHUNK_SIZE = 4 * (10 ** 7)  # 40Mb chunck size


def get_sha256(path: str) -> str:
    """Calculate and return the SHA256 hash of a given path

    :param path:    Path to file or directory
    :type path:     str

    :return:    SHA256 hash of the path
    :rtype:     str
    """
    if os.path.isdir(path):
        return (checksumdir.dirhash(path, 'sha256'))
    sha256_hash = hashlib.sha256()
    with open(path, 'rb') as f:
        for byte_block in iter(lambda: f.read(HASH_CHUNK_SIZE), b''):
            sha256_hash.update(byte_block)
        return (sha256_hash.hexdigest())


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <path>', file=sys.stderr)
        sys.exit(1)
    sha256 = get_sha256(sys.argv[1])
    print(sha256)
