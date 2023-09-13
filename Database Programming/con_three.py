from mysql.connector import connect, Error

try:
    con =  connect(
        host="localhost",
        database="todoapp",
        username="root",
        password=""
    )

    if con.is_connected():

        create_tbl = """create table laptops(
            id int primary key auto_increment,
            make varchar(100),
            price decimal(6, 2),
            purchase_date date);"""

        st = con.cursor()

        i = st.execute(create_tbl)

        print("Table created successfully")
        

except Error as e:
    print(e)