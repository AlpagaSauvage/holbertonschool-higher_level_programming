#!/usr/bin/python3

import MySQLdb
import sys

user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
cursor = db.cursor()
cursor.execute("SELECT state_id, cities.name, states.name FROM states JOIN\
    cities WHERE states.id = state_id")
result = cursor.fetchall()

for x in result:
    print(x)