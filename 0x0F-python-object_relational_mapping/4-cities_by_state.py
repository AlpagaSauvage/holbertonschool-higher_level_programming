#!/usr/bin/python3
"""4 cities by state"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect('localhost', user, pswd, name)
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    result = mycursor.fetchall()

    for x in result:
        print("{}".format(x))
