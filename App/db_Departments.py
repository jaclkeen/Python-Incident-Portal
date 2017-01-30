import psycopg2
from db_config import DB_Config

def GetDepartments():
    conn = psycopg2.connect(DB_Config())
    cur = conn.cursor()

    Departments = cur.execute( """ SELECT * FROM Departments """ )

    cur.close()
    conn.commit()

    conn.close()

    return Departments
