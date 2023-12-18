# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = {}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
        menu_item = input("Type menu item number: ")

            # 3. Check if the customer typed a number
        if menu_item.isdigit() and int(menu_item) in menu_items:
            item_name = menu_items[int(menu_item)]["Item name"]
            item_price = menu_items[int(menu_item)]["Price"]
            item_quantity = input("Type your order quantity: ")
            if item_quantity.isdigit():
                item_quantity = int(item_quantity)
                if item_name in order_list:
                    order_list[item_name]['Quantity'] += item_quantity
                else:
                    order_list[item_name] = {'Price': item_price, 'Quantity': item_quantity}
            else:
                print("You didn't select a number.")
        else:
            print(f"{menu_item} was not a menu item.")

    else:
        print("Invalid menu choice.") 

                    
    #while True:
        # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        # if keep_ordering.lower() == 'y':
            #break
                # Keep ordering

                # Exit the keep ordering question loop
                
                
                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order
            
                # Exit the keep ordering question loop
    if keep_ordering.lower() == 'n':
        print("Thanks for your order. Welcome comming back!")
        place_order = False
           

                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item, details in order_list.items():
    price = details['Price']
    quantity = details['Quantity']

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 25 - len(item) 
    item_spaces = " " * num_item_spaces
    formatted_price = f"${price:.2f}"
    num_price_spaces = 6 - len(formatted_price)
    price_spaces = " " * num_price_spaces
    print(f"{item}{item_spaces} | {formatted_price}{price_spaces} | {quantity}")

    # 9. Create space strings


    # 10. Print the item name, price, and quantity
# Order_total_cost = sum(details['Price'] * details['Quantity'] for details in order_list.values())

total_costs = [details['Price'] * details['Quantity'] for details in order_list.values()]
Order_total_cost = sum(total_costs)
print(f"Order total cost: ${Order_total_cost:.2f}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
