from mysql.connector import connect, Error

try:
    con =  connect(
        host="localhost",
        database="todoapp",
        username="root",
        password=""
    )

    if con.is_connected():

        insert_statement = """insert into laptops
        (make, price, purchase_date) values
        ('HP Folio', 15000, '2023-01-20'),
        ('Macbook Pro', 30000, '2023-08-22');"""

        st = con.cursor()

        i = st.execute(insert_statement)

        con.commit()

        print("Records added successfully")
        

except Error as e:
    print(e)