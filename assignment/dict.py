systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []
price = 0
def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
    print("Total :", price,"Baht")
