import psycopg2
from db_config import DB_Config

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
        CREATE TABLE Incident(
            IncidentId SERIAL PRIMARY KEY,
            CustomerId integer REFERENCES Customer,
            IncidentTypeName VARCHAR(100) NOT NULL,
            OrderIsReplaceable BOOLEAN NOT NULL,
            OrderIsRefundable BOOLEAN NOT NULL,
            InformationOfOrder BOOLEAN NOT NULL
        )
        """,
        """
        CREATE TABLE CustomerOrder(
            OrderId SERIAL PRIMARY KEY,
            OrderDate DATE NOT NULL,
            CustomerId integer REFERENCES Customer
        )
        """
    )

    return commands

def insertCommands():
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
        """
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


ExecuteDBCommands(CreateTableCommands())
ExecuteDBCommands(insertCommands())
