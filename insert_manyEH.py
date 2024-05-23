import mysql.connector
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="mysqldb")
    cursor=dbcon.cursor()
    sql='''insert into mysqltb values(%s,%s,%s);'''
    data=[(102,'kiran',45000),(103,'sunita',35000),(104,'anand',58000)]
    cursor.executemany(sql,data)
    dbcon.commit()
    print("data inserted successfuly")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()