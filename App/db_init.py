import psycopg2
from db_config import DB_Config
import datetime

# define db tables
def CreateTableCommands():
    commands = (
        """
        CREATE TABLE Departments(
            DepartmentId SERIAL PRIMARY KEY,
            DepartmentName text NOT NULL
        )
        """,
        """
        CREATE TABLE HRUser(
            AppUserId SERIAL PRIMARY KEY,
            FirstName VARCHAR(30) NOT NULL,
            LastName VARCHAR(30) NOT NULL,
            DepartmentId integer REFERENCES Departments
        )
        """,
        """
        CREATE TABLE Customer(
            UserId SERIAL PRIMARY KEY,
            FirstName VARCHAR(30) NOT NULL,
            LastName VARCHAR(30) NOT NULL
        )
        """,
        """
        CREATE TABLE CustomerOrder(
            OrderId SERIAL PRIMARY KEY,
            OrderDate VARCHAR(40) NOT NULL,
            CustomerId integer REFERENCES Customer,
            HRUserId integer REFERENCES HRUser
        )
        """,
        """
        CREATE TABLE Incident(
            IncidentId SERIAL PRIMARY KEY,
            OrderId INTEGER REFERENCES CustomerOrder,
            IncidentTypeName VARCHAR(100) NOT NULL,
            OrderIsReplaceable BOOLEAN NOT NULL,
            OrderIsRefundable BOOLEAN NOT NULL,
            InformationOfOrder BOOLEAN NOT NULL,
            Resolution TEXT
        )
        """
    )

    return commands

def InsertCommands():
    commands = (
        """
        INSERT INTO Departments VALUES (1, 'Apparel');
        """,
        """
        INSERT INTO Departments VALUES (2, 'Electronics');
        """,
        """
        INSERT INTO Departments VALUES (3, 'Toys & Games');
        """,
        """
        INSERT INTO Departments VALUES (4, 'Books');
        """,
        """
        INSERT INTO Departments VALUES (5, 'Home Furnishings');
        """,
        """
        INSERT INTO Customer (FirstName, LastName)
        VALUES ('Jacob', 'Keen')
        """,
        """
        INSERT INTO Customer (FirstName, LastName)
        VALUES ('Aaron', 'Keen')
        """
    )

    return commands

def CreatingOrders():
    today = datetime.date.today()
    today.strftime('%b %d %Y')

    commands = (
        """
        INSERT INTO CustomerOrder (OrderDate, CustomerId, HRUserId)
        VALUES ('{0}', 1, Null);
        """.format(today),
        """
        INSERT INTO CustomerOrder (OrderDate, CustomerId, HRUserId)
        VALUES ('{0}', 1, Null);
        """.format(today),
        """
        INSERT INTO CustomerOrder (OrderDate, CustomerId, HRUserId)
        VALUES ('{0}', 1, Null);
        """.format(today),
        """
        INSERT INTO CustomerOrder (OrderDate, CustomerId, HRUserId)
        VALUES ('{0}', 2, Null);
        """.format(today),
        """
        INSERT INTO CustomerOrder (OrderDate, CustomerId, HRUserId)
        VALUES ('{0}', 2, Null);
        """.format(today)
    )

    return commands

# create PostgreSQL tables
def ExecuteDBCommands(tableCommands):
    try:
        conn = psycopg2.connect(DB_Config())
        cur = conn.cursor()

        for command in tableCommands:
            cur.execute(command)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


# ExecuteDBCommands(CreateTableCommands())
# ExecuteDBCommands(InsertCommands())
# ExecuteDBCommands(CreatingOrders())
