#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    database.close()
