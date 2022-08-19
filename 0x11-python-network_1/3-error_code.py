#!/usr/bin/python3
"""error code"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
