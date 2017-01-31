from db_HrUser import FindHrUser, CreateNewHRUser
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

    print("\nEnter the number of the department you are in?")
    for department in GetDepartments():
        print (str(department[0]) + ": " + department[1])

    NewUserDepartmentId = raw_input("Department: > ")
    CreateNewHRUser(NewUserFirstName, NewUserLastName, NewUserDepartmentId)

def execute():
    hr_user = HomePrompt()

    if hr_user != 'new user':
        firstname = hr_user.split(" ")[0]
        lastname = hr_user.split(" ")[1]
        loggedInUser = FindHrUser(firstname, lastname)
        print ("\nWelcome back, " + loggedInUser + "!")
        IncidentMenu()
    else:
        ShowTitle()
        NewHrUserPrompt()

def IncidentMenu():
    ShowTitle()
    print("1: Create Incident")
    print("2: List My Incidents")
    print("3: Exit")

    IncidentMenuInput = raw_input("> ")

execute()
