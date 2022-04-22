#!/usr/bin/python3
"""What's my status? #0"""

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status/') as respons:
        html = respons.read()
        utf = html.decode(respons.headers.get_content_charset())

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", utf)
