#!/usr/bin/python3
"""3-my safe filter state"""
import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    pswd = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect('localhost', user, pswd, name)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states WHERE name = %s \
        ORDER BY states.id", (sys.argv[4],))
    result = mycursor.fetchall()

    for x in result:
        if x[1] == sys.argv[4]:
            print("{}".format(x))
