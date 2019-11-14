import sqlite3 as sql
import hashlib

def createPasswordCracker():
    #Add brute force itteration here:
    

    #Use this to check the password
    checkSQL(password)

##This checks the SQL file for the encrypted password and checks
##it against the variable passed to the method
def checkSQL(bruteForce):
    mydb = sql.connect("Passwords.db")
    c = mydb.cursor()
    c.execute("""SELECT ThePassword
FROM SecretPassword
WHERE Username == 'Admin'""")
    encryptedPassword=c.fetchone()
    mydb.close()
    password = bruteForce

    passEncoded=hashlib.sha224(bruteForce.encode())
    bruteForce=passEncoded.hexdigest()
    if bruteForce == encryptedPassword[0][:]:
        print("The password is {0}".format(password))
