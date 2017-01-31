import psycopg2
from db_config import DB_Config
from termcolor import colored

def FindHrUser(firstname, lastname):
    try:
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()
        data = (firstname.lower(), lastname.lower())
        query = """ SELECT FirstName, LastName FROM HRUser
                    WHERE lower(FirstName) LIKE %s AND lower(LastName) LIKE %s; """

        cur.execute(query, data)

        for u in cur:
            HrUser = u

        return HrUser


    except (Exception, psycopg2.DatabaseError) as error:
        print colored("\nCould not find user:{0} {1}".format(firstname, lastname), "red")
        return None

    finally:
        if conn is not None:
            conn.close()

def CreateNewHRUser(firstname, lastname, department):
    try:
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()
        data = (firstname, lastname, department)
        query = """ INSERT INTO HRUser (FirstName, LastName, DepartmentId) VALUES (%s, %s, %s); """

        cur.execute(query, data)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error creating a new HR user.", error)

    finally:
        if conn is not None:
            conn.close()

