import sqlite3
import bcrypt

# I used this file to insert a new user into the Users table
# before I implemented the registration page.

# Connect to the SQLite database
conn = sqlite3.connect('Hazardous Materials Database.db')
c = conn.cursor()

# User details
username = ''
name = ''
email = ''
password = ''
role = ''

# Hash the password
password = password.encode('utf-8')
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# Insert the new user into the Users table
c.execute("INSERT INTO Users (username, name, email, password, role) VALUES (?, ?, ?, ?, ?)",
          (username, name, email, hashed_password, role))

# Commit the changes and close the connection
conn.commit()
conn.close()


