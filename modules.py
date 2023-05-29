import sqlite3

import os
os.system('clear')


###################
####SQLite Data base
####################
# connect to the database
cone = sqlite3.connect('customer.db')
#create a cursor
c = cone.cursor()


'''
# create table
c.execute("""CREATE TABLE customer (
			first_name text,
			last_name text,
			email text
			)""")
'''
c.execute("INSERT INTO customer VALUES ('John','Elder','ralph042@gmail.com')")



# comit changes
cone.commit()





# close databse connection
cone.close()






