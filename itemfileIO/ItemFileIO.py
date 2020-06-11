# Item File IO
# Date Created: 6/11/20
# Last Modified: 6/11/20

INVENTORY_FILE = "items.txt"


def add_items():
    """
    Add items to inventory file
    """
    write_to_file = open(INVENTORY_FILE, "a")

    print("Please enter the following information:")
    item_name = input("Name: ")
    write_to_file.write(item_name + "\n")
    item_id = input("ID: ")
    write_to_file.write(item_id + "\n")
    item_cost = input("Cost: $")
    write_to_file.write(item_cost + "\n")
    item_quantity = input("Quantity: ")
    write_to_file.write(item_quantity + "\n")

    write_to_file.close()


def read_items():
    """
    Read in items from inventory file, print their data to console, and display total number of items
    """
    item_count = 0
    read_file = open(INVENTORY_FILE, "r")

    item_name = read_file.readline().rstrip()

    while item_name != '':
        item_id = int(read_file.readline().rstrip("\n"))
        item_cost = float(read_file.readline().rstrip("\n"))
        item_quantity = int(read_file.readline().rstrip("\n"))

        print("Name:", item_name)
        print("ID:", item_id)
        print("Cost: $", format(item_cost, ',.2f'), sep='')
        print("Quantity: ", item_quantity)
        item_count += item_quantity

        print("---")

        item_name = read_file.readline().rstrip()

    print(item_count, "items in stock")
    read_file.close()


def main():
    in_inventory = True

    print("Welcome to the item inventory system")
    print("1 | Add Items")
    print("2 | View Inventory")
    print("0 | Exit")

    while in_inventory:
        menu_selection = int(input("Action: "))
        while menu_selection != 1 and menu_selection != 2 and menu_selection != 0:
            menu_selection = int(input("Action: "))

        if menu_selection == 1:
            add_items()
        elif menu_selection == 2:
            read_items()
        elif menu_selection == 0:
            in_inventory = False
        else:
            print("Unknown command")

        print("=======")

    print("***Exiting***")


main()
