#!/usr/bin/python3
"""POST an email"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    mail = {"email": sys.argv[2]}

    query_string = urllib.parse.urlencode(mail)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
