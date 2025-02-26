# Ipmorts the core module
import ga_core

# Prints welcome message for app
print("Welcome to Tim's Grocery App! Let's Make Shopping Easier!\n")


def launch():
    """
    Starts the grocery list management program.

    This function serves as the main entry point for the program, allowing 
    the user to interact with the grocery list through a command-line 
    interface. The user can enter one of the following commands: 
    'add', 'remove', 'edit', 'list', 'export', or 'quit'.

    Commands:
        - add: Prompts the user to enter details for a new item and adds it 
          to the grocery list.
        - remove: Prompts the user for the name of an item to remove from 
          the grocery list.
        - edit: Prompts the user to enter updated details for an existing 
          item in the grocery list.
        - list: Displays all current items in the grocery list.
        - export: Displays items marked for purchase in the grocery list.
        - quit: Exits the program.

    The function runs in an infinite loop until the user chooses to quit 
    the program by entering the 'quit' command.
    
    Returns:
        None
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
            print(f"Item edited: Name: {name}, Store: {store}, Cost: {cost}, "
                  f"Amount: {amount}, Priority: {priority}, Buy: {buy}")
        
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
    """
    Prompts the user for various inputs related to a grocery item and
    validates the input.

    The function collects the following information:
    - Item name (string)
    - Store name (string or None if skipped)
    - Item cost (float or None if skipped)
    - Item quantity (integer or None if skipped)
    - Priority level (integer between 1 and 5 or None if skipped)
    - Buy decision (boolean: True for 'yes', False for 'no', or None if skipped)

    The function will continue to prompt the user until valid input is
    provided for each field.
    If the user inputs "skip" for any field, that field will be set 
    to None.

    Returns:
        tuple: A tuple containing the validated inputs in the following order:
            - name (str): The name of the item.
            - store (str or None): The name of the store or None if skipped.
            - cost (float or None): The cost of the item or None if skipped.
            - amount (int or None): The quantity of the item or None 
              if skipped.
            - priority (int or None): The priority level (1-5) or None 
              if skipped.
            - buy (bool or None): True if the user wants to buy the item,
              False if not, or None if skipped.
    """
    while True:
        name = input("Enter item name (i.e milk): ") 
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:
        store = input("Enter store name (i.e Walmart): ")
        if store == "skip":
            store = None
            break
        elif store:
            break
        print("Invalid input. Please add a valid store name")

    # Allows user to input the price
    while True:
        try:
            cost = input("Enter the price of the item (i.e 6.25): ")
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
            # Allows user to enter the quantity they want
            amount = input("Enter item quantity (i.e 5): ")
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
            priority = input("Enter priority (1-5): ")
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5: 
                priority = int(priority)
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")
    
    while True:
        buy = input("buy (yes or no): ")
        if buy.lower() == "yes":
            buy = True
            break
        elif buy.lower() == "no":
            buy = False
            break
        elif buy == "skip":
            buy = None
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'")

    return name, store, cost, amount, priority, buy

if __name__ == "__main__":
    launch()
