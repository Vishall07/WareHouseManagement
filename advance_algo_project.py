import uuid

class WareHouse:
    def __init__(self, name, location, max_capacity, available_capacity, phone_number):
        self.id = uuid.uuid4().int & (1<<64)-1
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.available_capacity = available_capacity
        self.phone_number = phone_number
    def __str__(self):
        return f"WareHouse name : {self.name} and its Situated at {self.location}"



class WareHouseManagement:
    
    def __init__(self):
        self.warehouses = []
        self.count = 0

    def add_warehouses(self,warehouse):
        self.warehouses.append(warehouse)
        self.count += 1
    
    def remove_warehouses(self, warehouse_id):
        for warehouse in self.warehouses:
            if(warehouse.id == warehouse_id):
                self.warehouses.remove(warehouse)
    
    def get_all_warehouses(self):
        for warehouse in self.warehouses:
            print(f"warehouse name is {warehouse.name} and its max capacity is {warehouse.max_capacity}")


warehouse_one = WareHouse("VRL","HUBLI",100, 100, "967376278323")
warehouse_two = WareHouse("VRL","Banglore",1000, 1000, "682623486324")
warehouse_three = WareHouse("VRL","PARIS",32653, 767, "873264836484")

warehouse_management = WareHouseManagement()

warehouse_management.add_warehouses(warehouse_one)
warehouse_management.add_warehouses(warehouse_two)
warehouse_management.add_warehouses(warehouse_three)

warehouse_management.get_all_warehouses()



