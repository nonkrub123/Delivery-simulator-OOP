class Person:
    def __init__(self,name):
        self.name = name
        self.introduce()
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")
    
class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.address = address
    
    def place_order(self,item):
        return DeliveryOrder(self.name,item)

class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.vehicle = vehicle
        
    def deliver(self,order,customer_name):
        print(f"{self.name} is delivering {order} to {customer_name} using {self.vehicle}.")
        return True


class DeliveryOrder:
    def __init__(self,customer,item):
        self.customer = customer
        self.item = item
        self.status = "preparing"
        self.driver = None

    def assign_driver(self,driver):
        self.driver = driver

    def pass_to_driver(self):
        if self.driver.deliver(self.item,self.customer):
            self.status = "delivered"
        
    def get_status(self):
        return f"Order for {self.item} → {self.status}"
    
    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver.name}"

Alice = Customer("Alice","test")
Bob = Customer("Bob","test")
driver = Driver("David","motorcycle")


order1 = Alice.place_order("Laptop")
order2 = Bob.place_order("Headphones")
order1.assign_driver(driver)
order2.assign_driver(driver)
print()
print(order1.summary())
print()
print(order2.summary())
print()

order1.pass_to_driver()
order2.pass_to_driver()
print()

print("Final Status:")
print(order1.get_status())
print(order2.get_status())