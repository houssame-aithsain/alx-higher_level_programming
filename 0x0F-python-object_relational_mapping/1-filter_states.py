#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':

    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], database=sys.argv[3])
    liSt = database.cursor()
    liSt.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY states.id ASC")
    rs = liSt.fetchall()
    for i in rs:
        print(i)
    rs.close()
    liSt.close()
