# Ipmorts the core module
import ga_core
print()

# Prints welcome message for app
print("Welcome to Tim's Grocery App! Let's Make Shopping Easier!")
print()

def launch():
    """ 
    This is the Begining of the program
    
     User enters one of the listed commands
      then enters each of the Items details

        """
    while True:
        command: str = input(
            "Enter a command (add, remove, edit, list, export, or quit): "
        )
       
        # Allows user to add new item to list
        if command == "add":  
           print("Enter details for new item")
           name, store, cost, amount, priority, buy = get_inputs()
           ga_core.add_item(
                            name = name,
                            store = store,
                            cost = cost,
                            amount = amount,
                            priority = priority,
                            buy = buy
                            )

        # Allows entering name of item to be removed from list
        if command == "remove":
            name: str = input("Enter name of item to remove: ") 

            ga_core.remove_item(name)

        # Allows editing items in list
        if command == "edit":
            name, store, cost, amount, priority, buy = get_inputs()
            ga_core.edit_item(name, store, cost, amount, priority, buy)

        # List the entire grocery list
        if command == "list":
            print("These are the current items in the grocery list")
            ga_core.list_item()

        # List items marked buy
        if command == "export":
            print("these are the current items in the buy list")
            ga_core.export_items()

        # Quits the program
        if command == "quit":
            break

def get_inputs():
            # User inputs name of item
            while True:
                name: str = input("Enter item name: ") 
                if name:
                    break
                print("Invalid input. Please enter a valid item")
            # User chooses the store for each item
            while True:
                store: str = input("Enter store name: ")
                if store == "skip":
                    store = None
                    break
                elif store:
                    store = store
                    break
                print("Invalid input. Please add a valid store name")
            # Allows user to input the price
            while True:
                try:
                    cost: float = (input("Enter the price of the \
item (i.e 6.25): "))
                    if cost == "skip":
                        cost = None
                        break
                    else: 
                        cost = float(cost)
                        break
                except ValueError:
                    print("Invalid input. please enter a valid price")
            
            while True:
                try:
                    # Allows user to enter the quanity they want
                    amount: int = (input("Enter item quantity (i.e 5): "))
                    if amount == "skip":
                        amount = None
                        break
                    else:
                        amount = int(amount)
                        break
                except ValueError:
                    print("Invalid input. please enter a valid quantity")
            # Sets priority between 1 and 5
            while True:
                try:
                    priority: int = (input("Enter priority (1-5): "))
                    if priority == "skip":
                        priority = None
                        break
                    elif 1 <= int(priority) <= 5: 
                        break
                    else:
                        print("Priority must be between 1 and 5")

                except ValueError:
                    print(
                        "Invalid input. Please enter a number between 1 and 5"
                        )
                    
            
            while True:
                try:
                    # Allows user to decide to buy the item or not
                    buy: str = input("buy (yes or no): ")
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