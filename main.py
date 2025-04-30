class Meal:
    """The product class representing a complete meal."""
    def __init__(self):
        self.burger = None
        self.burger_size = None
        self.toppings = []
        self.drink = None
        self.drink_size = None
        self.side = None

    def __str__(self):
        parts = []
        if self.burger:
            parts.append(f"{self.burger_size} {self.burger}" if self.burger_size else self.burger)
        if self.toppings:
            parts.append(f"with {', '.join(self.toppings)}")
        if self.drink:
            parts.append(f"+ {self.drink_size} {self.drink}" if self.drink_size else f"+ {self.drink}")
        if self.side:
            parts.append(f"+ {self.side}")
        return ' '.join(parts)


class MealBuilder:
    """The builder class that constructs the meal step by step."""
    def __init__(self):
        self.meal = Meal()

    def add_burger(self, burger_type):
        """Add a burger to the meal."""
        self.meal.burger = burger_type
        return self

    def with_size(self, size):
        """Set the size for the burger or drink."""
        if self.meal.burger:
            self.meal.burger_size = size
        elif self.meal.drink:
            self.meal.drink_size = size
        return self

    def add_topping(self, topping):
        """Add a topping to the burger."""
        self.meal.toppings.append(topping)
        return self

    def add_drink(self, drink_type):
        """Add a drink to the meal."""
        self.meal.drink = drink_type
        return self

    def add_side(self, side_item):
        """Add a side item to the meal."""
        self.meal.side = side_item
        return self

    def build(self):
        """Return the completed meal."""
        return self.meal


# Example usage
if __name__ == "__main__":
    # Build a simple meal with just a burger
    meal1 = MealBuilder().add_burger("Cheeseburger").build()
    print("Meal 1:", meal1)
    
    # Build a complete meal with all options
    meal2 = (MealBuilder()
             .add_burger("Bacon Burger")
             .with_size("Large")
             .add_topping("Lettuce")
             .add_topping("Tomato")
             .add_drink("Cola")
             .with_size("Medium")
             .add_side("Fries")
             .build())
    print("Meal 2:", meal2)
    
    # Build a meal with only some options
    meal3 = (MealBuilder()
             .add_burger("Veggie Burger")
             .add_topping("Avocado")
             .add_drink("Lemonade")
             .build())
    print("Meal 3:", meal3)
