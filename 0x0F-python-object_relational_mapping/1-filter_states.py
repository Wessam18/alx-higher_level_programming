#!/usr/bin/python3
"""import modules"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ to create connection"""
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE \
        name LIKE 'N%' ORDER BY id ASC")

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
