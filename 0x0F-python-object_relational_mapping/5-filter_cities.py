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
    
    sql_query = mycursor.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
