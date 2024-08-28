from menu import food_menu
import random

print("Welcome to the PyDate Simulator!")
date_name = input("Enter your date's name: ")
budget = float(input("What is your date budget for today? $"))

total_cost = 0

for category in food_menu:
    print(f"\n{category.capitalize()} Menu:")
    for item, price in food_menu[category].items():
        print(f"{item}: ${price:.2f}")
    
    your_choice = input(f"Enter the number of the {category} you want: ")
    # 1. gets dict for current food category. 2. converts keys into a list/array. 3. convert to int. 4. -1 because list starts at 0...
    your_item = list(food_menu[category].keys())[int(your_choice) - 1]
    your_price = food_menu[category][your_item]
    total_cost += your_price
    
    # same logic, but the date's side. This one is randomized because the user doesn't choose for the date.
    date_choice = random.choice(list(food_menu[category].keys()))
    date_price = food_menu[category][date_choice]
    total_cost += date_price
    
    print(f"You ordered: {your_item}")
    print(f"{date_name} ordered: {date_choice}")
    print(f"Total cost so far: ${total_cost:.2f}")

print(f"\nTotal bill: ${total_cost:.2f}")
if input("Do you agree to pay the bill? (yes/no): ").lower() == 'yes':
    remaining_budget = budget - total_cost
    print(f"You paid the bill. Remaining budget: ${remaining_budget:.2f}")
else:
    print(f"Welp... You walked off without paying anything, leaving {date_name} befuddled... Awkward.")

print("Play PyDate again soon. Cya!")
