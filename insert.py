import mysql.connector
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="mysqldb")
    cursor=dbcon.cursor()
    sql='''insert into mysqltb values(101,"rahul",45000)'''
    cursor.execute(sql)
    dbcon.commit()
    print("inserted successfully")
    
except:
    print("unable to connect")