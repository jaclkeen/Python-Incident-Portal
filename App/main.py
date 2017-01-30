import psycopg2
from db_config import DB_Config
from db_HrUser import FindHrUser
from db_Departments import GetDepartments

def ShowTitle():
    print ('\n=================================')
    print ('     CUSTOMER SERVICE PORTAL     ')
    print ('=================================')

def HomePrompt():
    ShowTitle()
    HrUser = raw_input("To start, enter your first name and last name. Type 'new user' to create a new user.\n> ")

    return HrUser

def NewHrUserPrompt():
    NewUserFirstName = raw_input("First name: > ")
    NewUserLastName = raw_input("Last name: > ")

    for index, department in enumerate(GetDepartments()):
        print(index, department.DepartmentName + "\n")


hr_user = HomePrompt()

if hr_user != 'new user':
    firstname = hr_user.split(" ")[0]
    lastname = hr_user.split(" ")[1]
    FindHrUser(firstname, lastname)
else:
    ShowTitle()
    NewHrUserPrompt()
