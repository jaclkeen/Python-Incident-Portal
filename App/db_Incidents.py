import psycopg2
from db_config import DB_Config

def CreateNewIncident(OrderNum, IncidentType, isReplaceable, isRefundable, isRequestingInformation):
    try:
        Incident = FindIncident(OrderNum)
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()

        NewData = (OrderNum, IncidentType, isReplaceable, isRefundable, isRequestingInformation)
        NewIncidentQuery = """
                      INSERT INTO Incident (OrderId, IncidentTypeName, OrderIsReplaceable, OrderIsRefundable, InformationOfOrder, Resolution)
                      VALUES (%s, %s, %s, %s, %s, Null)
                  """

        if Incident == None:
          NewIncident = cur.execute(NewIncidentQuery, NewData)
          cur.close()
          conn.commit()

          return FindIncident(OrderNum)
        else:
          return Incident

    except (Exception, psycopg2.DatabaseError) as error:
        return error

def FindIncident(OrderNum):
    try:
        Incident = None
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()
        FindData = (OrderNum)
        FindIncidentQuery = """
                    SELECT i.*, c.FirstName || ' ' || c.LastName
                    FROM Incident AS i
                    JOIN CustomerOrder AS co ON i.OrderId = co.OrderId
                    JOIN Customer AS c ON co.CustomerId = c.UserId
                    WHERE i.OrderId = %s
                """
        cur.execute(FindIncidentQuery, OrderNum)
        for i in cur:
          return i

    except (Exception, psycopg2.DatabaseError) as error:
      return error

def GetIncidents():
  return False