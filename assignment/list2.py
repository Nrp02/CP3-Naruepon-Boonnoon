menuList = []
totalprice = 0

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"Baht")
    print("Total :", totalprice,"Baht")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])  ##
        totalprice += int(menuPrice)

showBill()