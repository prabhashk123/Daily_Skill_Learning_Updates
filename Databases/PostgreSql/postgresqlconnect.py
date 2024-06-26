## Step1-pip install psycopg2-binary
# import psycopg2
# # Step-2 conection detall
# conn = psycopg2.connect(
#     dbname="ecomerse",
#     user="postgres", 
#     password="postgres", 
#     host="localhost", port=5432)
# # step-3 Create a Cursor Object:
# # Create a cursor object to execute SQL queries and retrieve data:
# cur=conn.cursor()
# # Step-4 Execute SQL Queries:
# cur.execute("SELECT * FROM main_product")
# #step-5(optional) Fetch Results (Optional):
# # If you're expecting data back from the query, call fetchone(),
# #  fetchall(), or fetchmany() on the cursor:
# # fetchone(): Retrieves one row as a tuple.
# # fetchall(): Retrieves all remaining rows as a list of tuples.
# # fetchmany(size): Retrieves size rows as a list of tuples.
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# # step-7 Close the Connection:
# # It's important to close the connection when you're finished to release resources:
# cur.close()
# conn.close()

"""Complete example"""
import psycopg2

# Replace with your credentials
DATABASE_NAME = "ecomerse"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "postgres"
HOST = "localhost"
PORT = 5432

try:
    conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()

    cur.execute("SELECT * FROM main_customer")
    rows = cur.fetchall()

    print("\nData from your_table:- ")
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()

    



