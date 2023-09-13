from mysql.connector import connect, Error

try:
    con =  connect(
        host="localhost",
        database="todoapp",
        username="root",
        password=""
    )

    if con.is_connected():

        info = con.get_server_info()
        print(info)

except Error as e:
    print(e)