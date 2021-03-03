""" This module """
from random import randint

class Item:
    """ Сlass by which you can describe the goods to be delivered """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """ Return information about item """
        return f'{self.name} - {self.price}'


class Location:
    """ Class that makes the address (city and post office) """
    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice



class Vehicle:
    """ Reflects the vehicle to which the delivery will be made"""
    def __init__(self, vehicleNo):
        self.vehicleNo = vehicleNo
        self.isAvailable = True



class Order(Vehicle):
    """ Contains all information about the order and the user """ 
    def __init__(self,user_name,city,postoffice,items):
        self.orderID = randint(1000000,9999999)
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items
        self.vehicle = None

    def calculate_amount(self):
        """ Calculates total price """
        total_price = 0
        for i in self.items:
            i = str(i)
            i = i.split(" - ")
            total_price += float(i[1])
        return total_price


    def assignVehicle(self, vehicle):
        """ Assign a vehicle """
        return vehicle.isAvailable


    def __str__(self):
        """ Return information about order """
        return f"Your order number is {self.orderID}"



class LogisticSystem:
    """ Main class, which stores all information about users, orders and transportation """\

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.orders_lst = []
    
    def placeOrder(self, my_order):
        """ Check if there is available car for delivering"""
        for vehicle in self.vehicles:
            if vehicle.isAvailable == True:
                self.orders_lst.append(my_order)
                vehicle.isAvailable = False
                return "Your order is ready to deliver"
        else:
            return "There is no available vehicle to deliver an order"

    def trackOrder(self, order_num):
        """ Return info about order """
        for my_order in self.orders_lst:

            if order_num == my_order.orderID:
                return f"Your order #{order_num} is sent to {my_order.city}. Total price: { my_order.calculate_amount() } UAH."
        else:
            return "No such order"



if __name__ == "__main__":
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)

    my_items = [Item('book',110), Item('chupachups',44)]
    my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)

    logSystem.placeOrder(my_order)
    print(logSystem.trackOrder(my_order.orderID))

    my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)

    logSystem.placeOrder(my_order2)
    print(logSystem.trackOrder(my_order2.orderID))

    my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)

    logSystem.placeOrder(my_order3)
    print(logSystem.trackOrder(my_order3.orderID))

