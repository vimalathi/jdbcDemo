import mysql.connector as mcon

conn = mcon.connect(user="hr_user",
                    password="itversity",
                    host="ms.itversity.com",
                    database="hr_db") #here we can use our database connections
cursor = conn.cursor()
query = "(select first_name, last_name, " \
        "case when commission_pct is null " \
        "then 'not eligible' " \
        "else commission_pct * salary " \
        "end commission_amt " \
        "from employees)"   #here we can use decode or any other function supported by the underlying database.
cursor.execute(query)
for i in list(cursor):
    print (i)
cursor.close()
conn.close()


