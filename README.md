# Custom Meal Order with Builder Design Pattern

This repository demonstrates the use of the **Builder Design Pattern** to create custom meal orders. The Builder pattern allows for the construction of complex objects (in this case, a meal) step by step, making it easy to add different items to the meal in any sequence.

## Problem Statement

In this example, we are building a system for customizing meal orders. Each meal consists of various items, such as:
- Burger
- Drink
- Side dish

Using the Builder Design Pattern, we can create a custom meal by adding specific items in a fluent and flexible manner.

## Components

### `Meal` Class
The `Meal` class represents a meal that consists of multiple items. It includes:
- A list (`items`) to hold the items in the meal.
- `add_item` method to add an item to the meal.
- `display_meal` method to print the meal's contents.

### `MealBuilder` Class
The `MealBuilder` class acts as a builder for the `Meal` object. It provides methods to add various items to the meal:
- `add_burger`: Adds a burger to the meal (e.g., Chicken or Veggie).
- `add_drink`: Adds a drink to the meal (e.g., Coke, Orange Juice).
- `add_side`: Adds a side dish to the meal (e.g., Fries).

The `build` method returns the constructed meal object.

## Usage Example

```python
meal_builder = MealBuilder()
custom_meal = meal_builder.add_burger("Chicken").add_drink("Coke").add_side("Fries").build()
custom_meal.display_meal()

meal_builder2 = MealBuilder()
meal2 = meal_builder2.add_burger("Veggie").add_drink("Orange Juice").build()
meal2.display_meal()
```
Example Output:
Meal:
- Chicken Burger
- Coke
- Fries

Meal:
- Veggie Burger
- Orange Juice

Benefits of the Builder Pattern
- Separation of Construction and Representation: The MealBuilder class handles meal construction, while the Meal class represents the final product.
- Fluent API: The builder provides a fluent interface, allowing for chaining method calls (e.g., add_burger("Chicken").add_drink("Coke")).
- Flexible Meal Construction: You can easily create different combinations of meals by adding only the items you want.
