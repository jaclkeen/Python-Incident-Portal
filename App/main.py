from termcolor import colored
from db_HrUser import FindHrUser, CreateNewHRUser
from db_Departments import GetDepartments
from db_Incidents import CreateNewIncident, FindIncident, GetIncidents, SaveResolution
from db_CustomerOrders import GetCustomerOrders

def ShowTitle():
    print ('\n=====================================')
    print ('       CUSTOMER SERVICE PORTAL       ')
    print ('=====================================')

def HomePrompt():
    print colored("- To start, enter your first and last name.\n- Or type 'new user' to create a new user.\n- Or press CTRL + C to quit.", "yellow")
    HrUser = raw_input("> ")

    if len(HrUser.split(" ")) == 2:
        return HrUser
    else:
        print colored("\nPlease enter a first and last name with a space in between them.", "red")
        execute()

def NewHrUserPrompt():
    print colored("Create a new user, or type 'back' to cancel.", "yellow")
    NewUserFirstName = raw_input("First name: > ")
    if NewUserFirstName == 'back': return execute()

    NewUserLastName = raw_input("Last name: > ")
    if NewUserLastName == 'back': return execute()

    print("\nWhat department you are in, {0}?".format(NewUserFirstName))
    for department in GetDepartments():
        print (str(department[0]) + ": " + department[1])

    NewUserDepartmentId = raw_input("Department: > ")
    if NewUserDepartmentId == 'back': return execute()

    CreateNewHRUser(NewUserFirstName, NewUserLastName, NewUserDepartmentId)
    print colored("\nUser {0} {1} was succesfully created!".format(NewUserFirstName, NewUserLastName), "yellow")
    execute()

def execute():
    ShowTitle()
    hr_user = HomePrompt()
    if hr_user != 'new user':
        firstname, lastname = hr_user.split(" ")[0], hr_user.split(" ")[1]
        loggedInUser = FindHrUser(firstname, lastname)
        if loggedInUser != None:
            print colored("\nWelcome back, " + loggedInUser[0] + "!", "white")
            IncidentMenu(loggedInUser)
        else:
            execute()
    else:
        ShowTitle()
        NewHrUserPrompt()

def IncidentMenu(CurrentHrUser):
    ShowTitle()
    print("1: Create Incident")
    print("2: List My Incidents")
    print("3: Back")

    IncidentMenuInput = raw_input("> ")

    if (int(IncidentMenuInput) == 1) or (int(IncidentMenuInput) == 2):
        return IncidentMenuFunctions[IncidentMenuInput](CurrentHrUser)
    elif int(IncidentMenuInput) == 3:
        return IncidentMenuFunctions[IncidentMenuInput]()
    else:
        print colored("\nInvalid command", "red")
        IncidentMenu(CurrentHrUser)

def CreateIncidentPrompt(CurrentHrUser):
    print colored("\nEnter customer name (<first> <last>)", "yellow")
    CustomerName = raw_input("> ")

    CustomerOrders = GetCustomerOrders(CustomerName)

    if len(CustomerOrders) == 0:
        print colored("\n{0} has no orders.".format(CustomerName), "red")
        IncidentMenu(CurrentHrUser)
    else:
        print colored("\nOrder Number\tCustomer Name\tOrder Date", "yellow")
        for order in CustomerOrders:
            print str(order[0]) + "\t\t" + str(order[4]) + "\t" + str(order[1])

        print colored("\nPlease select an order number.", "yellow")
        print colored("Or type 'back' to return to the incident menu.", "yellow")
        OrderNumOption = raw_input("> ")
        ChooseIncidentTypePrompt(OrderNumOption, CurrentHrUser, CustomerName)

def ChooseIncidentTypePrompt(OrderNumOption, CurrentHrUser, CustomerName):
    if OrderNumOption == 'back':
        IncidentMenu(CurrentHrUser)

    if FindIncident(OrderNumOption) == None:
        print colored("\nChoose incident type:","yellow")
        print ("1. Defective Product")
        print ("2. Product Not Delivered")
        print ("3. Request Information")
        print ("4. Back")

        IncidentPromptSelection = raw_input("> ")
        if int(IncidentPromptSelection) != 4:
            CreateIncident(OrderNumOption, IncidentPromptSelection, CurrentHrUser, CustomerName)
        else:
            print colored("\nInvalid command", "red")
            ChooseIncidentTypePrompt(OrderNumOption, CurrentHrUser, CustomerName)
    else:
        ShowIncident(OrderNumOption, CurrentHrUser)

def CreateIncident(OrderNum, IncidentSelection, CurrentHrUser, CustomerName):
    if int(IncidentSelection) == 4:
        return IncidentMenu(CurrentHrUser)
    elif int(IncidentSelection) == 1:
        NewIncident = CreateNewIncident(OrderNum, "Defective Product", True, True, False, CurrentHrUser[2])
    elif int(IncidentSelection) == 2:
        NewIncident = CreateNewIncident(OrderNum, "Product Not Delivered", False, True, False, CurrentHrUser[2])
    else:
        NewIncident = CreateNewIncident(OrderNum, "Request Information", False, False, True, CurrentHrUser[2])
    ShowIncident(OrderNum, CurrentHrUser)

def ShowIncident(OrderNum, CurrentHrUser):
    Incident = FindIncident(OrderNum)
    print Incident
    print colored("\nIncident:\n", "yellow") + "======================================================="
    print colored("Customer Name: ", "yellow") + Incident[8] + "\t\t" + colored("Order Number: ","yellow") + str(Incident[1])
    print colored("Incident Type: ", "yellow") + Incident[3] + colored("\n\nLabels:", "yellow")
    if Incident[4] == True: print("* This order is refundable")
    if Incident[5] == True: print("* This order is replaceable")
    if Incident[6] == True: print("* Non-Tranactional incident")
    print colored("\nResolution:", "yellow")
    if Incident[7] == None:
        Resolution = raw_input("> ")
        SaveResolution(Resolution, OrderNum)
        print colored("Your resolution on order #{0} was succesfully saved!", "yellow").format(OrderNum)
        IncidentMenu(CurrentHrUser)
    else:
        print("{0}\n=======================================================").format(Incident[7])
        print colored("\nPress enter to return to the incident menu.","yellow")
        back = raw_input("> ")
        IncidentMenu(CurrentHrUser)


IncidentMenuFunctions = {'1': CreateIncidentPrompt, '2': GetIncidents, '3': execute}
execute()
