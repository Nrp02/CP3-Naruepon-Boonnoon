class customer:
    name = ""
    last_name = ""
    age = 0

    def addCart(self):
        print("Added to", self.name, self.last_name+"'s cart")

customer1 = customer()
customer1.name = "John"
customer1.last_name = "Carty"
customer1.addCart()

customer2 = customer()
customer2.name = "Jane"
customer2.last_name = "Martin"
customer2.addCart()

customer3 = customer()
customer3.name = "Alice"
customer3.last_name = "Dan"
customer3.addCart()

customer4 = customer()
customer4.name = "Bob"
customer4.last_name = "Mores"
customer4.addCart()