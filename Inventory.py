inventory = {}

def add_product(name, quantity, price):
    # Implement the function to add or update a product in the inventory
  name = input("Enter the product name: ")
  quantity = float(input("Enter the quantity: "))
  price = float(input("Enter the price:$ "))

  if name in inventory:
      inventory[name]['quantity'] += quantity
      inventory[name]['price'] = price
  else:
      inventory[name] = {'quantity': quantity, 'price': price}
  print(f"{quantity} {name} has been added to the inventory.")
  return inventory

def display_inventory():
# Implement the function to display the inventory 
  display = [print(f"{name}: Quantity - {values['quantity']}, Price - ${values['price']}")
             for name, values in inventory.items()]

  return display

def calculate_total_value():
    # Implement the function to calculate and display the total value of the inventory
  inventory_total = sum(values["quantity"] * values["price"] 
                        for values in inventory.values())
  print(f"Total value of the inventory is: ${inventory_total}")
  return inventory_total

def update_quantity(name, new_quantity):
    # Implement the function to update the quantity of a specific product
  name = input("enter the product name: ")
  new_quantity = int(input("entern new quantity: "))

  if name in inventory:
      inventory[name]["quantity"] = new_quantity
      print(f"new quantity of {name} is {new_quantity}")
  else:
      print(f"{name} is not in the inventory")
  return inventory
def remove_product(name):
    # Implement the function to remove a product from the inventory
  name = input("enter product name: ")
  if name in inventory:
      del inventory[name]
      print(f"{name} has been removed from the inventory")
  else:
      print(f"{name} is not in the inventory")
      return inventory

# Demonstrate the functionality in the main part of your script
# Add products, display inventory, update quantities, remove products, and calculate total value

while True:
  print("Welcome to the inventory, what would you like to do?")
  print("""
  1. Add product,
  2. display inventory
  3. calculate inventory total
  4. update quantity
  5. remove product
  6. exit
""")
  break
while True: 
  task = int(input("Enter a task: "))

  if task == 1:
    add_product("name", "quantity", "price")
  elif task == 2:
    display_inventory()
  elif task == 3:
    calculate_total_value()
  elif task == 4:
    update_quantity("name", "new_quantity")
  elif task == 5:
    remove_product("name")
  elif task == 6:
    break
  else:
    print("Invalid task. Please enter a valid task number.")