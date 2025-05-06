username = input("username: ")
password = input("password: ")

if username == "N" and password == "2704":
    print("\n Welcome to Sky shop: " + username + "!")
    print("\n Please choose the product you would like:")
    print("\n1. Product A: 100 Baht")
    print("2. Product B: 200 Baht")
    print("3. Product C: 300 Baht")
    print("\n4. Product A and B: 100 Baht and 200 Baht")
    print("5. Product A and C: 100 Baht and 300 Baht")
    print("6. Product B and C: 200 Baht and 300 Baht")
    print("7. Product A, B and C: 100 Baht, 200 Baht and 300 Baht")

    userselect = input("\n Please select a product (1-7): ")
    if userselect == "1":
        print("\nYou have selected Product A: 100 Baht")
        price = 100
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 100 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "2":
        print("\nYou have selected Product B: $200 Baht")
        price = 200
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 200 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "3":
        print("\nYou have selected Product C: $300 Baht")
        price = 300
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 300 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "4":
        print("\nYou have selected Product A and B: 100 Baht and 200 Baht")
        price = 300
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 100 Baht + 200 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "5":
        print("\nYou have selected Product A and C: 100 Baht and 300 Baht")
        price = 400
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 100 Baht + 300 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "6":
        print("\nYou have selected Product B and C: 200 Baht and 300 Baht")
        price = 500
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 200 Baht + 300 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    elif userselect == "7":
        print("\nYou have selected Product A, B and C: 100 Baht, 200 Baht and 300 Baht")
        price = 600
        vat = price * 0.07
        total_price = price + vat
        print("\nPrice 100 Baht + 200 Baht + 300 Baht + VAT: 7%")
        print("\nTotal price including VAT:", total_price, "Baht")

    else:
        print("\nInvalid selection. Please choose a product between 1 and 7.")

else:
    if username != "N" and password != "2704":
        print("Error! Please enter the correct username and password.")
    elif username != "N":
        print("Username not found.")
    elif password != "2704":
        print("Your password is incorrect. Please try again.")
    else:
        print("Error!")