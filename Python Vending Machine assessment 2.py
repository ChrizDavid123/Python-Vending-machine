print("Welcome to the vending machine made by Chrizlen Dave P. Rollan from cyber security level 4! Pick any item you want to dispense...")

menu = {
    "A1": ("Lays chips", 3),
    "A2": ("Lacnor milk", 4),
    "A3": ("Lacnor milk chocolate", 7),
    "B1": ("Lipton iced tea", 5),
    "B2": ("Pepsi", 6),
    "B3": ("Hello Panda", 5),
    "C1": ("Water", 1),
    "C2": ("Mountain Dew", 4),
    "C3": ("Skittles", 5),
    "D1": ("M&M's", 6),
    "D2": ("Pringles", 7),
    "D3": ("Cheetos", 3),
    "E1": ("Doritos", 3),
    "E2": ("Maltasers", 5),
    "E3": ("Feastables", 20),
}
# Displays the items in the menu
print("\nMenu:")
for code, (item, price) in menu.items():
        print(f"{code}. {item}: AED {price}")

# Asks to input balance and makes sure its a whole number
while True:    
     balance_input = input("\nPlease input your balance (Whole numbers only!): ")
     if balance_input.isdigit():
           balance = int(balance_input)
           break 
     else: 
          print("Invalid Response. Please enter a whole number...")

# Asks user to input item code
while True:
     print(f"\nCurrent Balance: AED {balance}")
     try:
          buy = input("Please input an item code: ").upper()
     except ValueError:
          print("Invalid Response. Please enter a valid item code...")
          continue
 
     # Checks if buy is part of the menu and then calculates how much balance remains
     if buy in menu:
          item, price = menu[buy]
          if balance >= price:
               balance -= price
               print(f"\n{item} (AED {price}) has been dispensed!")
               print(f"Current Balance: {balance}")  
          else:
               print(f"Insufficient Balance. {item} costs AED {price}. Thank you for your time...\nHere is your change: AED {balance} \nclosing program...")
               break       
     else:
          print("Invalid item code. Please try again...")
          continue

     # Checks if balance is 0 or bellow
     if balance <= 0:
          print(f"Insufficient Balance. Thank you for your time... \nHere is your change: AED {balance} \nClosing program...")
          break 
     
     # Asks the user if they want to purchase another item. 
     repeat = input("Would you like to purchase another item? y/n: ").lower()
     if repeat != "y":
          print("Thank you for choosing us! Have a nice day...")
          if balance > 0:
               print(f"Here is your change: AED {balance}")
               break
          else:
               break