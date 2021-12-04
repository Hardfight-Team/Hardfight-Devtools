# External imports
from typing import Dict
import urllib.request
import json
import sys


def read_url_as_json(url: str) -> Dict:
    """Reads the content of an URL as a JSON and returns it
    :note: No sanity checks performed, caller should catch exceptions

    :param url: URL to read the JSON
    :type url:  str

    :return:    Content of the URL as a JSON
    :rtype:     Dict
    """
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
        result = json.loads(content)
        return (result)


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <url>', file=sys.stderr)
        sys.exit(1)
    json_dict = read_url_as_json(sys.argv[1])
    print(json_dict)
