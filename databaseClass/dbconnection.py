import sqlite3

#conn = sqlite3.connect('database/operation.db')
# create opeartion.db file if it does not exist and connect 
# if operation.db file exist already it connect directly to connection.db 


# function to create table 
def createTable():
    conn = sqlite3.connect('database/operation.db')
    c =conn.cursor()    # this is used to run and execute sql command 
    c.execute("""CREATE TABLE IF NOT EXISTS CALCULATOR(  
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NUM1 TEXT NOT NULL,
                            NUM2 TEXT NOT NULL,
                            OPERATOR TEXT NOT NULL,
                            RESULT TEXT NOT NULL);""")
    conn.commit()
    conn.close()

def insertData(_num1 ,_num2,_op,_result):
    conn = sqlite3.connect('database/operation.db')
    c =conn.cursor()
    c.execute("INSERT INTO CALCULATOR (NUM1, NUM2, OPERATOR, RESULT) VALUES(" + str(_num1) + "," + str(_num2) + ",'" + _op + "'," + str(_result) + ");")
    conn.commit()
    conn.close()

def deleteData():
    conn = sqlite3.connect('database/operation.db')
    c =conn.cursor()
    c.execute("DELETE FROM CALCULATOR;")
    conn.commit()
    conn.close()

def showAllData():
    conn = sqlite3.connect('database/operation.db')
    c =conn.cursor()
    c.execute("select * from CALCULATOR") 
    temp =c.fetchall()
    return temp


