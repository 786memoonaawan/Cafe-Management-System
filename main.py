# Define the menu of restaurant
menu = {
  'Pizza': 800,
  'Pasta': 600,
  'Burger': 400,
  'Fries': 200,
  'Salad': 350,
  'Sandwich': 250,
  'Coffee': 300,
}

# Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs.800\nPasta: Rs.600\nBurger: Rs.400\nFries: Rs.200\nSalad: Rs.350\nSandwich: Rs.250\nCoffee: Rs.300")

order_total = 0
# 300 + 350 = 650

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
   order_total += menu[item_1] # 0 + 600 = 600
   print(f"Your item {item_1} has been added in your order")

else:
  print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
  item_2 = input("Enter the name of second item =")
  if item_2 in menu:
    order_total += menu[item_2]
    print(f"Item {item_2} has been added to order")
  else:
    print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is {order_total}")