import uuid
from tabulate import tabulate
from operator import attrgetter

class WareHouse:
    def __init__(self, name, location, max_capacity, phone_number):
        self.id = uuid.uuid4().int & (1<<64)-1
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.available_capacity = max_capacity
        self.phone_number = phone_number

    def __str__(self):
        return f"WareHouse name: {self.name} and its situated at {self.location}"

class WareHouseManagement:
    def __init__(self):
        self.warehouses = []

    def add_warehouses(self, warehouse):
        self.warehouses.append(warehouse)
        print(f"Warehouse '{warehouse.name}' added successfully!\n")

    def remove_warehouses(self, warehouse_id):
        for warehouse in self.warehouses:
            if warehouse.id == warehouse_id:
                self.warehouses.remove(warehouse)
                print("Warehouse removed successfully!\n")
                return
        print("Warehouse ID not found!\n")

    def get_all_warehouses(self):
        if not self.warehouses:
            print("No warehouses available.\n")
            return
        header = ["ID", "NAME", "LOCATION", "MAX_CAPACITY", "AVAILABLE_CAPACITY"]
        warehouse_table = []
        for warehouse in self.warehouses:
            temp = [warehouse.id, warehouse.name, warehouse.location, warehouse.max_capacity, warehouse.available_capacity]
            warehouse_table.append(temp)
        print(tabulate(warehouse_table, headers=header, tablefmt="fancy_grid"))

    def add_items_to_warehouse(self, quantity, warehouse_id):
        for warehouse in self.warehouses:
            if warehouse.id == warehouse_id:
                if warehouse.available_capacity < quantity:
                    print(f"Not enough capacity. Available capacity is: {warehouse.available_capacity}\n")
                else:
                    warehouse.available_capacity -= quantity
                    print(f"{quantity} items added to warehouse '{warehouse.name}'.\n")
                return
        print("Warehouse ID not found!\n")

    def sort_based_on_max_capacity(self):
        self.warehouses.sort(key=attrgetter('max_capacity'), reverse=True)
        print("Warehouses sorted by maximum capacity:\n")
        self.get_all_warehouses()

    def sort_based_on_available_capacity(self):
        self.warehouses.sort(key=attrgetter('available_capacity'), reverse=True)
        print("Warehouses sorted by available capacity:\n")
        self.get_all_warehouses()

def main():
    warehouse_management = WareHouseManagement()

    while True:
        print("\n===== Warehouse Management System =====")
        print("1. Add Warehouse")
        print("2. Remove Warehouse")
        print("3. View All Warehouses")
        print("4. Add Items to a Warehouse")
        print("5. Sort Warehouses by Maximum Capacity")
        print("6. Sort Warehouses by Available Capacity")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter warehouse name: ")
            location = input("Enter warehouse location: ")
            while True:
                try:
                    max_capacity = int(input("Enter warehouse max capacity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for max capacity.")
            phone_number = input("Enter warehouse phone number: ")
            warehouse = WareHouse(name, location, max_capacity, phone_number)
            warehouse_management.add_warehouses(warehouse)

        elif choice == '2':
            try:
                warehouse_id = int(input("Enter warehouse ID to remove: "))
                warehouse_management.remove_warehouses(warehouse_id)
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        elif choice == '3':
            warehouse_management.get_all_warehouses()

        elif choice == '4':
            try:
                warehouse_id = int(input("Enter warehouse ID to add items: "))
                quantity = int(input("Enter quantity of items to add: "))
                warehouse_management.add_items_to_warehouse(quantity, warehouse_id)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID and quantity.")

        elif choice == '5':
            warehouse_management.sort_based_on_max_capacity()

        elif choice == '6':
            warehouse_management.sort_based_on_available_capacity()

        elif choice == '7':
            print("Exiting Warehouse Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
