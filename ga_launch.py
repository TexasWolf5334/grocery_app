# Ipmorts the core module
import ga_core
print()
# Prints welcome message for app
print("Welcome to Tim's Grocery App! Let's Make Shopping Easier!")
print()
def launch():
    while True:
        command = input("Enter a command (add, remove, edit, list, export, or quit): ")
       
        # allows user to add new item to list
        if command == "add":  
           print("Enter details for new item")
           name, store, cost, amount, priority, buy = get_inputs()
           ga_core.add_item(name=name, store=store, cost=cost, amount=amount, priority=priority, buy=buy)

        # allows entering name of item to be removed from list
        if command == "remove":
            name = input("Enter name of item to remove: ")

            ga_core.remove_item(name)

        # allows editing items in list
        if command == "edit":
            name, store, cost, amount, priority, buy = get_inputs()
            ga_core.edit_item(name, store, cost, amount, priority, buy)

        # list the entire grocery list
        if command == "list":
            print("These are the current items in the grocery list")
            ga_core.list_item()

        # list items marked buy
        if command == "export":
            print("these are the current items in the buy list")
            ga_core.export_items()

        # quits the program
        if command == "quit":
            break

def get_inputs():
            # user inputs name of item
            while True:
                name = input("Enter item name: ")
                if name:
                    break
                print("Invalid input. Please enter a valid item")
            # user chooses the store for each item
            while True:
                store = input("Enter store name: ")
                if store == "skip":
                    store = None
                    break
                elif store:
                    store = store
                    break
                print("Invalid input. Please add a valid store name")
            # allows user to input the price
            while True:
                try:
                    cost = (input("Enter the price of the item (i.e 6.25): "))
                    if cost == "skip":
                        cost = None
                        break
                    else: 
                        cost = float(cost)
                        break
                except ValueError:
                    print("Invalid input. please enter a valid price")
            # alows user to enter the quanity tthey want
            while True:
                try:
                    amount = (input("Enter item quantity (i.e 5): "))
                    if amount == "skip":
                        amount = None
                        break
                    else:
                        amount = int(amount)
                        break
                except ValueError:
                    print("Invalid input. please enter a valid quantity")
            # sets priority between 1 and 5
            while True:
                try:
                    priority = (input("Enter priority (1-5): "))
                    if priority == "skip":
                        priority = None
                        break
                    elif 1 <= int(priority) <= 5: 
                        break
                    else:
                        print("Priority must be between 1 and 5")

                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5")
            # allows user to decide to buy the item or not
            while True:
                try:
                    buy = input("buy (yes or no): ")
                    if buy.lower() == "yes":
                        buy =  True
                        break
                    elif buy.lower() == "no":
                        buy = False
                        break
                    elif buy == "skip":
                        buy = "skip"
                        break
                    else:
                        print("Invalid input. Please enter true or false")
                except ValueError:
                    print("Invalid input. Please enter 'true' or 'false'")

            return name, store, cost, amount, priority, buy


if __name__ == "__main__":
    launch()