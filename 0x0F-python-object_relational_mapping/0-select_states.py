#!/usr/bin/python3
"""0-select state"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY states.id")
    result = mycursor.fetchall()

    for x in result:
        print(x)
