# Custom Meal Order Builder (Builder Pattern in Python)

A clean implementation of the Builder design pattern for constructing custom meal orders with flexible options.

## Overview

This project demonstrates how to use the Builder Pattern to create customizable meal orders where:
- You can select only the options you care about
- The construction process is clean and intuitive
- The code is easy to extend with new options

## Features

- Build meals with any combination of:
  - Burgers (with optional size specification)
  - Toppings (multiple can be added)
  - Drinks (with optional size specification)
  - Side items
- Fluent builder interface for easy chaining
- Clear string representation of the final meal

## Usage
```
from meal_builder import MealBuilder

# Simple meal with just a burger
meal1 = MealBuilder().add_burger("Cheeseburger").build()

# Complete meal with all options
meal2 = (MealBuilder()
         .add_burger("Bacon Burger")
         .with_size("Large")
         .add_topping("Lettuce")
         .add_topping("Tomato")
         .add_drink("Cola")
         .with_size("Medium")
         .add_side("Fries")
         .build())

# Meal with only some options
meal3 = (MealBuilder()
         .add_burger("Veggie Burger")
         .add_topping("Avocado")
         .add_drink("Lemonade")
         .build())

print(meal1)
print(meal2)
print(meal3)
```

Example Output
- Cheeseburger
- Large Bacon Burger with Lettuce, Tomato + Medium Cola + Fries
- Veggie Burger with Avocado + Lemonade
