class vehicle:
    licensecode = ""
    serialcode = ""
    def turnonairconditioner(self):
        print("Turning on air conditioner")

class car(vehicle):
    def welcome(self):
        print("Welcome !")

class PickUp(vehicle):
    def welcome(self):
        print("Welcome to pick up")

class Van(vehicle):
    def welcome(self):
        print("Welcome to van")

class EstateCar(vehicle):
    def welcome(self):
        print("Welcome to estate car")

car1 = car()
car1.turnonairconditioner()
car1.welcome()

van1 = Van()
van1.turnonairconditioner()
van1.welcome()

estatecar1 = EstateCar()
estatecar1.turnonairconditioner()
estatecar1.welcome()

pickup1 = PickUp()
pickup1.turnonairconditioner()
pickup1.welcome()