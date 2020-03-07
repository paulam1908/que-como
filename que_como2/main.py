import pymysql

""" CONECCION A BASE DE DATOS """
conn=pymysql.connect(
host='localhost',
            user='root',
            password='',
            db='mysql'
)
cursor = conn.cursor()

cursor.execute("SELECT VERSION()")

for row in cursor:
    print("base de datos conectada")

cursor.close()
conn.close()
