inventory = {}

def manage_inventory():
    while True:
        print("inventory management system")
        print("1. add item")
        print("2.view inventory")
        print("3.update item quantity")
        print("4.exit")
        choice = input ("enter choice(1/2/3/4):")

if __name__ == "__main__":
    manage_inventory()

    if choice == 1:
        def add_item(item, quantity):
            if item in inventory:
                inventory[item] = quantity+inventory[item]
            else:
                inventory[item]= quantity

def view_inventory():
    for item, quantity in inventory():
        print (item,quantity)

item = input()
quantity = int(input())     
add_item(item, quantity)
print (inventory)

view_inventory()