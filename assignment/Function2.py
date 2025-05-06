def login():
    while True:
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
        if usernameInput == "admin" and passwordInput == "1234":
            print("Login Success, Welcome to iShop!")
            return True
        else:
            print("Wrong username or password. Please try again.")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Exit")

def menuSelect():
    userSelected = 0
    while userSelected not in [1, 2, 3]:
        userSelected = int(input(">>"))
        if userSelected in [1, 2, 3]:
            return userSelected
        else:
            print("Invalid input. Please try again.")

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
while True:
    showMenu()
    userSelected = menuSelect()
    if userSelected == 1:
        print(vatCalculator(int(input("Total Price : "))))
    elif userSelected == 2:
        print(priceCalculator())
    elif userSelected == 3:
        print("Thank you for using iShop! See you again!")
        break
    else:
        print("Invalid input. Please try again.")