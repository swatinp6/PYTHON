import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="mysqldb")
    cursor=dbcon.cursor()
    sql='''create table mysqltb(eid int,ename varchar(30),esal int);'''
    cursor.execute(sql)
    print("table created successfully")
    
except:
    print("unable to connect")

