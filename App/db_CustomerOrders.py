import psycopg2
from db_config import DB_Config

def GetCustomerOrders(CustomerName):
    Orders = list()
    conn = psycopg2.connect(DB_Config())
    cur = conn.cursor()
    data = (CustomerName.split(" ")[0], CustomerName.split(" ")[1])
    query = """
                SELECT co.*, c.FirstName || ' ' || c.LastName
                FROM CustomerOrder AS co
                JOIN Customer AS c
                ON co.CustomerId = c.UserId
                WHERE lower(c.FirstName) LIKE lower(%s)
                AND lower(c.LastName) LIKE lower(%s)
            """

    cur.execute(query, data)

    for o in cur:
        Orders.append(o)

    cur.close()
    conn.commit()

    conn.close()

    return Orders
