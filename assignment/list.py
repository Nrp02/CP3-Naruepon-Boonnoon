menuList = []
priceList = []
totalprice = 0

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number],"Baht")
    print("Total :", totalprice,"Baht")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
        totalprice += int(menuPrice)

showBill()