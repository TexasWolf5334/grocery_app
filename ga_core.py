# list of items for grocery list
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
# this block of code allows adding new items to grocery list
def add_item(name, store, cost, amount, priority, buy):
    item = {"name": name, "store": store, "cost": cost, "amount": amount,
             "priority": priority, "buy":  buy}
    grocery_list.append(item)
# this block of code allows removing items from grocery list
def remove_item(name):
    index = get_index_from_name(name)
    grocery_list.pop(index)

# allows change at any index in the list
def edit_item(name, store=None, cost=None, amount=None,
               priority=None, buy="skip"):
    
    index = get_index_from_name(name)

    # this block of code keeps original values for unchanged indexes
    old_item = grocery_list[index]

    if not store:
        store= old_item["store"]

    if not cost:
        cost= old_item["cost"]

    if not amount:
        amount= old_item["amount"]

    if not priority:
        priority = old_item["priority"]

    if  buy == "skip":
        buy = old_item["buy"]

    item = {"name": name, "store": store, "cost": cost, "amount": amount, 
            "priority": priority, "buy":  buy}

    grocery_list[index] = item
    
# this block of code exports buy items to a buy list 
def export_items():
    buy_list = []
    
    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)
    # Prints buy list
    if buy_list:
        for item in buy_list:
            print(
                f"name: {item["name"]} - store: {item["store"]} - "
                f"cost: ${item["cost"]} - amount: {item["amount"]} - "
                f"priority: {item["priority"]}"
            )
        
        total_cost = calculate_total_cost(buy_list, round_cost=True)


def get_index_from_name(name):
    index = 0

    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1

# Print each item in the grocery list
def list_item():
    for item in grocery_list:
        print(item)
# calculates total cost of grocery list with tax
def calculate_total_cost(grocery_list, round_cost=False, tax=0.0825):
    total_cost = 0

    for item in grocery_list:
        # Calculate the cost
        cost = item["amount"] * item["cost"]
        # Add the cost to total cost
        total_cost += cost
    # Round the cost
    if round_cost:
        total_cost = round(total_cost)    
    # Add the tax
    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost
# Prints the total cost of grocery list
    print(f"The total cost is ${total_cost:.2f}")
    return total_cost



