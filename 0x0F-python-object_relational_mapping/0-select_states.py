#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
