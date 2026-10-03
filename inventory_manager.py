current_inventory = {
    "name" : ["laptop", "mouse", "keyboard"],
    "price" : [1200, 25.50, 45],
    "stock" : [14, 40, 25]
}

def add_product(name, price, stock):
    current_inventory["name"].append(name)
    current_inventory["price"].append(price)
    current_inventory["stock"].append(stock)
    return f"Product '{name}' added successfully."

def update_stock(name, new_stock):
    if name in current_inventory["name"]:
        index = current_inventory["name"].index(name)
        current_inventory["stock"][index] = new_stock
        return f"Stock for '{name}' updated to {new_stock}."
    else:
        return f"Product '{name}' not found in inventory."

def search_stock(name):
    if name in current_inventory["name"]:
        index = current_inventory["name"].index(name)
        stock = current_inventory["stock"][index]
        return f"Stock for '{name}': {stock}"
    else:
        return f"Product '{name}' not found in inventory."

def search_product(name): 
    if name in current_inventory["name"]:
        index = current_inventory["name"].index(name)
        price = current_inventory["price"][index]
        stock = current_inventory["stock"][index]
        return f"Product '{name}': Price - ${price}, Stock - {stock}"
    else:
        return f"Product '{name}' not found in inventory."

def display_inventory():
    inventory_list = []
    for i in range(len(current_inventory["name"])):
        product_info = {
            "name": current_inventory["name"][i],
            "price": current_inventory["price"][i],
            "stock": current_inventory["stock"][i]
        }
        inventory_list.append(product_info)
    return inventory_list

import json 
import os 

FILENAME = "inventory.json" 

def load_inventory():
    if os.path.exists(FILENAME): 
        with open(FILENAME, "r") as file: 
            data = json.load(file) 
            current_inventory["name"] = data.get("name", []) 
            current_inventory["price"] = data.get("price", []) 
            current_inventory["stock"] = data.get("stock", [])

def save_inventory():
    with open(FILENAME, "w") as file: 
        json.dump(current_inventory, file)

def show_menu():
    print ("""----------- MENU -----------
    1. Display All Products
    2. Add Product
    3. Update Stock
    4. Search Product
    5. Save Inventory
    6. Exit
    ----------------------------""")

load_inventory()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print(display_inventory())

    elif choice == "2":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        print(add_product(name, price, stock))

    elif choice == "3":
        name = input("Enter product name to update stock: ")
        new_stock = int(input("Enter new stock quantity: "))
        print(update_stock(name, new_stock))

    elif choice == "4":
        name = input("Enter product name to search: ")  
        print(search_product(name))

    elif choice == "5":
        save_inventory()
        print("Inventory saved successfully.")

    elif choice == "6":
        save_inventory()
        print("Exiting the program. Inventory saved.")
        break
