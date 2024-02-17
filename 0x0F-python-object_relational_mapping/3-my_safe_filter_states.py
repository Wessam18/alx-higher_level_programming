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

    state_name = sys.argv[4]

    mycursor = mydb.cursor()

    my_sql = "SELECT * FROM states WHERE \
        name = %s ORDER BY id ASC"

    mycursor.execute(my_sql, (state_name,))

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
