class Rental:
    #initializing name the number of available scooters and customers
    def __init__(self,name,num_scooters):
        self.name = name
        self.num_scooters = num_scooters
        self.customers = {}

# taking in name and customer scooter number ordered to calculate number of scooters left in stock
    def rent_hourly(self,name,cust_scooters):
        if cust_scooters > self.num_scooters:
            print("Scooter number invalid, please enter a different number.")
        else:
            self.customers[name] = {"hourly": cust_scooters}
            self.num_scooters = self.num_scooters - cust_scooters
            print("Rent Completed Successfully")

    def rent_daily(self, name, cust_scooters):
        if cust_scooters > self.num_scooters:
            print("Scooter number invalid, please enter a different number.")
        else:
            self.customers[name] = {"daily": cust_scooters}
            self.num_scooters = self.num_scooters - cust_scooters
            print("Rent Completed Successfully")

    def rent_weekly(self,name,cust_scooters):
        if cust_scooters > self.num_scooters:
            print("Scooter number invalid, please enter a different number.")
        else:
            self.customers[name] = {"weekly": cust_scooters}
            self.num_scooters = self.num_scooters - cust_scooters
            print("Rent Completed Successfully")
# calculating total price from type of time number of scooters ordered an discount, then adding the returned amount of scooters back to the available amount
    def invoice_return(self,name):
        if name in self.customers:
            for time in self.customers[name]:
                if time == "hourly":
                    scooter_count = self.customers[name]["hourly"]
                    self.num_scooters = self.num_scooters + scooter_count
                    print("You rented " + str(scooter_count) + " scooters.")
                    if 3 <= scooter_count <= 5:
                        print("You received a discount of " + str((5*(scooter_count*.30))) + " reaching a total of " + str((5*(scooter_count * .70))))
                    else:
                        print("your invoice total is" + str(5*(scooter_count)))
                elif time == "daily":
                    scooter_count = self.customers[name]["daily"]
                    self.num_scooters = self.num_scooters + scooter_count
                    print("You rented " +str(scooter_count) +" scooters.")
                    if 3 <= scooter_count <= 5:
                        print("You received a discount of " + str((20*(scooter_count*.30))) + " reaching a total of " + str((20*(scooter_count * .70))))
                    else:
                        print("your invoice total is" +  str(20*(scooter_count)))
                elif time == "weekly":
                    scooter_count = self.customers[name]["weekly"]
                    self.num_scooters = self.num_scooters + scooter_count
                    print("You rented " + str(scooter_count) + " scooters.")
                    if 3 <= scooter_count <= 5:
                        print("You received a discount of " + str((50*(scooter_count*.30))) + " reaching a total of " + str((50*(scooter_count * .70))))
                    else:
                        print("your invoice total is" + str(50*(scooter_count)))
        else:
            print("Please enter name again")


if __name__ == "__main__":
    shop = Rental("Scooter Shop", 50)
    while True:
        task = input("Select input task number. 1. show the number of scooters available , 2. rent, 3. return, 4. close the store ")
        if task == "1":
            print("number of available scooters is " + str(shop.num_scooters))
        elif task == '2':
            time = input("Would you like an 1. Hourly 2. Daily or 3. Weekly rental? ")
            count = int(input("How many scooters would you like to rent? "))
            name = input("Enter your name: ")
            if time == '1':
                shop.rent_hourly(name, count)
            elif time == '2':
                shop.rent_daily(name, count)
            elif time == '3':
                shop.rent_weekly(name, count)
            else:
                print("Sorry, something went wrong")
        elif task == '3':
            if shop.customers:
                for name in shop.customers:
                    print(name)
                names = input("Enter your name: ")
                shop.invoice_return(names)
            else:
                print("You cannot perform this action.")
        elif task == '4':
            break
        else:
            print("Error")
print("end")




