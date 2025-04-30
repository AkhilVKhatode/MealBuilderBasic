class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_meal(self):
        print("Meal:")
        for item in self.items:
            print(f"- {item}")

class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_burger(self, burger_type):
        self.meal.add_item(f"{burger_type} Burger")
        return self

    def add_drink(self, drink_type):
        self.meal.add_item(f"{drink_type}")
        return self

    def add_side(self, side_type):
        self.meal.add_item(f"{side_type}")
        return self
    
    def build(self):
        return self.meal

# Usage
meal_builder = MealBuilder()
custom_meal = meal_builder.add_burger("Chicken").add_drink("Coke").add_side("Fries").build()
custom_meal.display_meal()

meal_builder2 = MealBuilder()
meal2 = meal_builder2.add_burger("Veggie").add_drink("Orange Juice").build()
meal2.display_meal()
