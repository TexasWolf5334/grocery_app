def Calculate_total_cost(grocery_list, round_cost=False, tax=0.0825):
    total_cost = 0

    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    if round_cost:
        total_cost = round(total_cost)    

    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    print(f"The total cost is ${total_cost:.2f}")
    return total_cost

