import psycopg2 as pg2
try:
    conn = pg2.connect(dbname="dvdrental", user="postgres", password="123456")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("SELECT * FROM payment")
data = cur.fetchmany(10)
print(data)
