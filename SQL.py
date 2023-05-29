
import sqlite3


import os
os.system('clear')


#create data base or connect to database
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()


# Create table

c.execute("""CREATE TABLE customer(
			first_name text,
			last_name text,
			email text,
			)""")


# 	Commit
conn.commit()



#close database connection
conn.close()





