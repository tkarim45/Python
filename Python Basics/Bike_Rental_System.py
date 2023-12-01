from datetime import datetime, timedelta

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f'Currently Available Stock is: {self.stock}')
        return self.stock

    def RentBikeOnHourlyBasis(self, no_of_bikes_needed):

        if no_of_bikes_needed <= 0:
            print('Kindly, Enter Positive Number')
        elif no_of_bikes_needed > self.stock:
            print(f'Sorry we currently have {self.stock} available Bikes at the Moment.')
        else:
            now = datetime.now()
            print(f'You have rented {no_of_bikes_needed} bike(s) on hourly basis today at {now.hour} hours.')
            print('You will be charged $5 for each hour per bike')

            self.stock -= no_of_bikes_needed
            return now

    def RentBikeOnDailyBasis(self, no_of_bikes_needed):
        if no_of_bikes_needed <= 0:
            print('Kindly, Enter Positive Number')
        elif no_of_bikes_needed > self.stock:
            print(f'Sorry we currently have {self.stock} available Bikes at the Moment.')
        else:
            now = datetime.now()
            print(f'You have rented {no_of_bikes_needed} bike(s) on hourly basis today at {now.hour} hours.')
            print('You will be charged $20 for each day per bike')

            self.stock -= no_of_bikes_needed
            return now

    def RentBikeOnWeeklyBasis(self, no_of_bikes_needed):
        if no_of_bikes_needed <= 0:
            print('Kindly, Enter Positive Number')
        elif no_of_bikes_needed > self.stock:
            print(f'Sorry we currently have {self.stock} available Bikes at the Moment.')
        else:
            now = datetime.now()
            print(f'You have rented {no_of_bikes_needed} bike(s) on hourly basis today at {now.hour} hours.')
            print('You will be charged $60 for each week per bike')

            self.stock -= no_of_bikes_needed
            return now

    def returnBike(self, request):
        rentalTime, rentalBasis, numofBikes = request
        bill = 0

        if rentalTime and rentalBasis and numofBikes:
            self.stock += numofBikes
            now = datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numofBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.seconds / 3600) * 20 * numofBikes
            elif rentalBasis == 3:
                bill = round(rentalPeriod.seconds / 3600) * 60 * numofBikes

            if 3 <= numofBikes >= 5:
                bill = bill * 0.7
                print(f'Your total bill is: {bill}')

        else:
            print("You didn't rented a bike")
            return None

    def __str__(self):
        return 'Remaining Stock is: ' + str(self.stock)


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent")

        try:
            bikes = int(bikes)
        except ValueError:
            print("Enter Positive Number")
            return -1

        if bikes < 1:
            print("You should least rent 1 bike")
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        if self.rentalTime and self.rentalBasis and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0


shop = BikeRental(50)
print(shop)
customer1 = Customer()
customer1.rentalBasis = 1
customer1.bikes = 5
customer1.rentalTime = datetime.now() + timedelta(hours=-4)
request1 = customer1.returnBike()
shop.returnBike(request1)

customer2 = Customer()
customer2.rentalBasis = 2
customer2.bikes = 5
customer2.rentalTime = datetime.now() + timedelta(hours=-23)
request2 = customer2.returnBike()
shop.returnBike(request2)

customer3 = Customer()
customer3.rentalBasis = 3
customer3.bikes = 100
customer3.rentalTime = datetime.now() + timedelta(hours=-30)
request3 = customer3.returnBike()
shop.returnBike(request3)