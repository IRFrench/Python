import sqlite3 as sql
import hashlib

##This changes the passed variable into an encrypted password
def createPassword(x):
    password=x
    passEncoded=hashlib.sha224(password.encode())
    password=passEncoded.hexdigest()
    return password

##This creates an SQL file with the passed Password
def passwordIntoSQL(password):
    mydb = sql.connect("Passwords.db")
    c = mydb.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS SecretPassword (Username, ThePassword)""")
    c.execute("""INSERT INTO SecretPassword
VALUES ('Admin', '{0}')""".format(password))
    mydb.commit()
    mydb.close()

##This will run the methods createing an SQL file
##with Admin, Password123 as the values
password = createPassword("Password123")
passwordIntoSQL(password)
