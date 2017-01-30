import psycopg2
from db_config import DB_Config

def FindHrUser(firstname, lastname):
    try:
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()

        HrUser = cur.execute(
            """
                SELECT *
                FROM HRUser
                WHERE lower(FirstName) LIKE {0} AND lower(LastName) LIKE {1}
            """.format(firstname.lower(), lastname.lower()))

        return HrUser

    except (Exception, psycopg2.DatabaseError) as error:
        print("Could not find user: {0} {1}".format(firstname, lastname))

    finally:
        if conn is not None:
            conn.close()

# def CreateNewUser(firstname, lastname, department):

