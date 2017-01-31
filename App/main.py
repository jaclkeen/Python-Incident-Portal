from termcolor import colored
from db_HrUser import FindHrUser, CreateNewHRUser
from db_Departments import GetDepartments
from db_Incidents import CreateNewIncident, GetIncidents

def ShowTitle():
    print ('\n=================================')
    print ('     CUSTOMER SERVICE PORTAL     ')
    print ('=================================')

def HomePrompt():
    HrUser = raw_input("To start, enter your first name and last name. Type 'new user' to create a new user.\n> ")

    if len(HrUser.split(" ")) == 2:
        return HrUser
    else:
        print colored("\nPlease enter a first and last name with a space in between them.", "red")
        execute()

def NewHrUserPrompt():
    NewUserFirstName = raw_input("First name: > ")
    NewUserLastName = raw_input("Last name: > ")

    print("\nEnter the number of the department you are in?")
    for department in GetDepartments():
        print (str(department[0]) + ": " + department[1])

    NewUserDepartmentId = raw_input("Department: > ")
    CreateNewHRUser(NewUserFirstName, NewUserLastName, NewUserDepartmentId)

def execute():
    ShowTitle()
    hr_user = HomePrompt()
    if hr_user != 'new user':
        firstname, lastname = hr_user.split(" ")[0], hr_user.split(" ")[1]
        loggedInUser = FindHrUser(firstname, lastname)
        if loggedInUser != None:
            print colored("\nWelcome back, " + loggedInUser[0] + "!", "yellow")
            IncidentMenu()
        else:
            execute()
    else:
        ShowTitle()
        NewHrUserPrompt()

def IncidentMenu():
    ShowTitle()
    print("1: Create Incident")
    print("2: List My Incidents")
    print("3: Exit")

    IncidentMenuInput = raw_input("> ")
    IncidentMenuFunctions[IncidentMenuInput]()

IncidentMenuFunctions = {'1': CreateNewIncident, '2': GetIncidents, '3': execute}

execute()
