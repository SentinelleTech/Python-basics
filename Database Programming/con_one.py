from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        username="root",
        password=""
    ) as con:

        print(con)

except Error as e:
    print(e)