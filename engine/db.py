#                                   ----- Database Code -----
import sqlite3
import csv

#                                   --- building connection --- 
con = sqlite3.connect("jarvis.db")

#                                          --- cursor --- 
cursor = con.cursor()

#                                  --- create a table sys_command --- 
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#                                  --- create a table web_command --- 
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#                                  --- create a contact table --- 
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

#                                  ---  insert into table --- 

# --- sys_command table entries: --- 
# query = "INSERT INTO sys_command VALUES (null,'telegram', 'C:\\Users\\bodhi\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')"
# cursor.execute(query)
# con.commit()  # saving the data on db upto this instance


# --- web_command table entries: --- 
# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()  # saving the data on db upto this instance


# --- importing contacts and inserting into contacts table---
# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 32]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

## Commit changes and close connection
# con.commit()
# con.close()


#                           --- Search contacts from database ---
# query = 'Sriza'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

#                           ------ Adding email of contacts ---------
# cursor.execute('''UPDATE contacts SET email = 'shu7773sea@gmail.com' WHERE id = 13''')
# con.commit()