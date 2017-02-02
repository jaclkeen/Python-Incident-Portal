import psycopg2
from db_config import DB_Config

def GetDepartments():
    Departments = list()
    conn = psycopg2.connect(DB_Config())
    cur = conn.cursor()

    cur.execute( """ SELECT * FROM Departments """ )

    for d in cur:
        Departments.append(d)

    cur.close()
    conn.commit()

    conn.close()

    return Departments
