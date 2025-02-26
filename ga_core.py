"""
grocery_list_core

This module serves as the core functionality for managing a grocery list.
It provides essential operations for creating, updating, and managing grocery
items, allowing users to maintain a structured list of items to be purchased
from various stores.

Functions:
    add_item(name: str, store: str, cost: float, amount: int, priority: int,
            buy: bool) -> None
        Adds a new item to the provided grocery list.

    remove_item(name: str)
        Removes an item from the provided grocery list by its name.
        Returns True if the item was successfully removed, False otherwise.

    edit_item(name: str, store: str = None, cost: float = None, amount: int = None,
               priority: int = None, buy: bool = "skip") -> None:
        Updates the details of an existing item in the grocery list.
        Accepts keyword arguments for the fields to be updated.

   export_items():
    Exports and prints a list of items marked for purchase from the 
    grocery list.

    This function iterates through a predefined `grocery_list`, 
    checking each item to determine if it is marked for purchase 
    (i.e., if the "buy" key is set to True). 
    If an item is marked for purchase, it is added to a `buy_list`.

    list_item():
        Displays the current grocery list with all items and their details.

Attributes:
    grocery_list (list[dict[str, float | int | str | bool]]): A list of dictionaries,
    where each dictionary represents a grocery item with the following keys:
        - "name" (str): The name of the grocery item.
        - "store" (str): The name of the store where the item can be purchased.
        - "cost" (float): The cost of a single unit of the item.
        - "amount" (int): The quantity of the item to be purchased.
        - "priority" (int): The priority level of the item for purchase (lower numbers indicate higher priority).
        - "buy" (bool): A flag indicating whether the item should be bought (True) or not (False).
"""

grocery_list: list[dict[str, float | int | str | bool]] = [
    {"name": "milk", "store": "Walmart", "cost": 2.50, "amount": 2,
      "priority": 1, "buy": True},
    {"name": "bread", "store": "Walmart", "cost": 3.00, "amount": 2,
      "priority": 1, "buy": True},
    {"name": "eggs", "store": "Walmart", "cost":  6.10, "amount": 1,
      "priority": 1, "buy": True},
    {"name": "peanut butter", "store": "Costco", "cost": 2.80, "amount": 1,
      "priority": 3, "buy": False},
    {"name": "chicken", "store": "Costco", "cost": 12.25, "amount": 1,
      "priority": 2, "buy": False}
]

def add_item(name: str, store: str, cost: float, amount: int, priority: int,
            buy: bool) -> None:
    """
    Adds an item to the grocery list.

    Parameters:
    name (str): The name of the item.
    store (str): The store where the item can be purchased.
    cost (float): The cost of the item.
    amount (int): The quantity of the item to be added.
    priority (int): The priority level of the item (e.g., 1 for high priority).
    buy (bool): A flag indicating whether the item should be bought (True)
    or not (False).

    Returns:
    None: This function does not return a value; it modifies the grocery
    list in place.
    """
    item = {
        "name": name,
        "store": store,
        "cost": cost, 
        "amount": amount,
        "priority": priority, 
        "buy":  buy
    }
    grocery_list.append(item)


def remove_item(name: str):
        """
    Removes an item from the grocery list by its name.

    This function searches for the item with the specified name in the
    grocery list and removes it if found. If the item is not found,
    an error message is printed.

    Parameters:
    name (str): The name of the item to be removed from the grocery list.

    Returns:
    None: This function does not return a value; it modifies the grocery
    list in place.
    """
        index = get_index_from_name(name)
        if index != -1:
          grocery_list.pop(index)


def edit_item(name: str, store: str = None, cost: float = None, 
              amount: int = None, priority: int = None, 
              buy: bool = "skip") -> None:
    """
    Edits an existing item in the grocery list.

    This function updates the details of an item in the grocery list based
    on the provided parameters. If a parameter is not provided (i.e., it is
    None or "skip"), the original value from the grocery
    list will be retained.

    Parameters:
    name (str): The name of the item to edit.
    store (str, optional): The new store name or None to keep the original.
    cost (float, optional): The new cost or None to keep the original.
    amount (int, optional): The new quantity or None to keep the original.
    priority (int, optional): The new priority level or None 
    to keep the original.
    buy (bool): The new buy decision or "skip" 
    to keep the original.

    Returns:
    None: This function does not return a value; it modifies the grocery
    list in place.

    Raises:
    IndexError: If the item with the specified name is not found
    in the grocery list.
    """
    index = get_index_from_name(name)

    if index == -1:
        raise IndexError(f"Item '{name}' not found in the grocery list.")

    old_item = grocery_list[index]

    if store is None:
        store = old_item["store"]

    if cost is None:
        cost = old_item["cost"]

    if amount is None:
        amount = old_item["amount"]

    if priority is None:
        priority = old_item["priority"]

    if buy == "skip":
        buy = old_item["buy"]

    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": buy
    }

    grocery_list[index] = item
    

def export_items():
    """
    Exports and prints a list of items marked for purchase from the 
    grocery list.

    This function iterates through a predefined `grocery_list`, 
    checking each item to determine if it is marked for purchase 
    (i.e., if the "buy" key is set to True). 
    If an item is marked for purchase, it is added to a `buy_list`. 

    After compiling the `buy_list`, the function prints the details 
    of each item in the list, including the item's name, store, cost,
    amount, and priority. If there are no items to buy, nothing is printed.

    Additionally, the function calculates the total cost of the items in the 
    `buy_list` by calling the `calculate_total_cost` function, with an option 
    to round the cost if specified.

    Returns:
        None
    """
    buy_list = []
    
    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)
    
    if buy_list:
        for item in buy_list:
            print(
                f"name: {item["name"]} - store: {item["store"]} - "
                f"cost: ${item["cost"]} - amount: {item["amount"]} - "
                f"priority: {item["priority"]}"
            )
        
        total_cost = calculate_total_cost(buy_list, round_cost = True)


def get_index_from_name(name):
    """
    Retrieves the index of an item in the grocery list based on its name.

    This function searches through a predefined `grocery_list` to find the 
    first occurrence of an item with a name that matches the provided 
    `name` parameter. If a match is found, the function returns the 
    index of that item in the list. If no match is found, the function 
    will return None.

    Parameters:
        name (str): The name of the item to search for in the grocery list.

    Returns:
        int or None: The index of the item in the grocery list if found; 
                     otherwise, None if the item is not found.
    """
    
    index = 0

    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1
            
    return None  # Return None if the item is not found

def list_item():
    """
    Prints all items in the grocery list.

    This function iterates through the `grocery_list` and 
    prints each item to the console.
    
    Returns:
        None
    """
    for item in grocery_list:
        print(item)

def calculate_total_cost(grocery_list, round_cost=False, tax=0.0825):
    """
    Calculates the total cost of items in the grocery list, including
    optional tax and rounding.

    This function computes the total cost of all items in the provided 
    `grocery_list`. Each item's cost is determined by multiplying its 
    amount by its cost per unit. The function can also apply a tax rate 
    and round the total cost if specified.

    Parameters:
        grocery_list (list): A list of dictionaries, where each dictionary 
                             contains the keys "amount" and "cost" 
                             for each item.
        round_cost (bool, optional): If True, the total cost will be rounded 
                                      to the nearest whole number. 
                                      Defaults to False.
        tax (float, optional): The tax rate to be applied to the total cost. 
                               Defaults to 0.0825 (8.25%).

    Returns:
        float: The total cost of the grocery list, including tax and rounding 
               if applicable.

    Prints:
        The total cost formatted to two decimal places.
    """
    
    total_cost = 0

    for item in grocery_list:
        # Calculate the cost
        cost = item["amount"] * item["cost"]
        # Add the cost to total cost
        total_cost += cost
        
    # Round the cost
    if round_cost:
        total_cost = round(total_cost, 2)    
    
    # Add the tax
    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    # Prints the total cost of grocery list
    print(f"The total cost is ${total_cost:.2f}")
    return total_cost



