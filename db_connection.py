import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=DB_CONFIG["dbname"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"]
        )
        return connection



    except Exception as e:
        print(f"Unable to connect to the database: {e}")
        return None
