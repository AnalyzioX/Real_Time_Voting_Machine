import pymysql

try:
    conn = pymysql.connect(
        user = 'root',
        password='',
        host='localhost',
        database='voting_db',
    cursorclass=pymysql.cursors.DictCursor
    )
    if conn.open:
        print("connected to MySQL database")
        conn.close()
except pymysql.MemoryError as err:
    print(f"Error:{err}")