import psycopg2

from database.database_interface import Database





class PostgresDatabase(Database):


    def get_data(self) -> list[dict]:
        pass

    def insert_data(self) -> None:
        pass


conn = psycopg2.connect(
    host="localhost",
    database="dwh",
    user="sql_dwh",
    password="sql_dwh")

cur = conn.cursor()
cur.execute("""Select *
from contact.contacts""")

# display the PostgreSQL database server version
data = cur.fetchall()
print(data)
print("Fatih")