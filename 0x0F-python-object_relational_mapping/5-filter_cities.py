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
    sql_query = ("SELECT cities.name FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id ASC")
    arg = sys.argv[4]
    mycursor.execute(sql_query, (arg,))
    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
