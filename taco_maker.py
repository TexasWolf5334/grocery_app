 #Day 6 Organization and Modularity Exercises 1-6
class TacoMaker:
    def __init__(self):
        """
        Initializes a new instance of the TacoMaker class.

        Attributes:
            taco (str): The type of taco being made.
            ingredients (list): A list to store the ingredients for the taco.
            quantities (list): A list to store the quantities for each 
ingredient.
            prices (dict): A dictionary mapping ingredient names to 
their prices.
        """
        self.taco = ""
        self.ingredients = [] 
        self.quantities = []  
        self.prices = {
            "Chicken": 2.50,
            "Beef": 3.00,
            "Veggie": 1.50,
            "Cheese": 0.50,
            "Lettuce": 0.30,
            "Tomato": 0.40,
            "Salsa": 0.60,
            "Guacamole": 1.00,
        }

    def run(self):
        """Main method to orchestrate the taco-making process."""
        print("Welcome to the Taco Maker!")
        self.taco = self.taco_type()
        self.gather_ingredients()
        total_cost = self.calculate_total_cost()
        self.print_grocery_list(total_cost)
        self.assemble_taco()
        

    def taco_type(self):
        """Get the type of taco from the user."""
        while True:
            taco = input("What kind of taco are you making? (e.g., chicken,\
beef, veggie): ")
            if taco.strip():  # Ensure the input is not empty
                return taco
            print("Please enter a valid taco type.")

    def gather_ingredients(self):
        """Gather ingredients and their quantities from the user."""
        while True:
            ingredient = input("Enter an ingredient (or 'done' to stop): ")
            if ingredient.lower() == 'done':
                if self.ingredients:  # Ensure at least one ingredient is added
                    return
                else:
                    print("You need to add at least one ingredient.")
            elif ingredient.strip():  # Ensure the input is not empty
                quantity = input(f"Enter the quantity for {ingredient}: ")
                self.add_item(ingredient, quantity)
            else:
                print("Please enter a valid ingredient.")

    def add_item(self, ingredient, quantity):
        """Add an ingredient and its quantity to the lists."""
        self.ingredients.append(ingredient)
        self.quantities.append(quantity)

    def calculate_total_cost(self):
        """Calculate the total cost of the ingredients."""
        total_cost = 0
        for ingredient in self.ingredients:
            # Use a default price of 1.00 if the ingredient is not in
            # the prices dictionary
            total_cost += self.prices.get(ingredient, 1.00)
        return total_cost

    def print_grocery_list(self, total_cost):
        """Print the grocery list and total cost."""
        print("\nGrocery List:")
        for ingredient, quantity in zip(self.ingredients, self.quantities):
            print(f"- {quantity} of {ingredient}")
        print(f"Total Cost: ${total_cost:.2f}")

    def assemble_taco(self):
        """Assemble and display the taco."""
        print(f"\nAssembling your {self.taco} taco with the following\
ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"\nYour {self.taco} taco is ready! Enjoy!")

   
if __name__ == "__main__":
    taco_maker = TacoMaker()
    taco_maker.run()


