''''
Jamison Murphy
Dr. Ray Toal
CMSI 662

'''
price = [20.10, 50.25, 30.50, 40.75, 10.15]

name = (input("Please enter name for order: "))
print("Name: ", name)

number = (input("Please enter phone number for order: "))
print("Phone Number: ", number)

print("What would you like to Purchase ")
print("1. [C]lothes $20.10 each ")
print("2. [E]lectronics $50.25 each ")
print("3. [H]ousedecor $30.50 each ")
print("4. [M]edications $40.75 each ")
print("5. [F]ood $10.15 each ")
print("6. [X]Check out ")
choice = (input())
subTotal = 0

while choice == 'C' or 'E' or 'H' or 'M' or 'F':
    if choice == 'C':
      print(" How many would you like to buy? ")
      quantity = int(input())
      subTotal += price[0] * quantity
      print("Subtotal: ", subTotal)
      print("Do you want to add these to the cart? (y/n) ")
      cart = (input())
      if cart == 'y':
        subTotal = subTotal
      else:
        print("Adding items? (y/n) ")
        edit = (input())
        if edit == 'y':
          print("How many? ")
          additions = int(input())
          subTotal -= price[0] * quantity
          quantity += additions
          subTotal += price[0] * quantity
          print("Subtotal: ", subTotal)
        else:
          print("Removing items? (y/n) ")
          edit = (input())
          if edit == 'y':
            print("How many? ")
            subtractions = int(input())
            subTotal -= price[0] * quantity
            quantity -= subtractions
            subTotal += price[0] * quantity
            print("Subtotal: ", subTotal)
    elif choice == 'E':
      print(" How many would you like to buy? ")
      quantity = int(input())
      subTotal += price[1] * quantity
      print("Subtotal: ", subTotal)
      print("Do you want to add these to the cart? (y/n) ")
      cart = (input())
      if cart == 'y':
        subTotal = subTotal
      else:
        print("Adding items? (y/n) ")
        edit = (input())
        if edit == 'y':
          print("How many? ")
          additions = int(input())
          subTotal -= price[1] * quantity
          quantity += additions
          subTotal += price[1] * quantity
          print("Subtotal: ", subTotal)
        else:
          print("Removing items? (y/n) ")
          edit = (input())
          if edit == 'y':
            print("How many? ")
            subtractions = int(input())
            subTotal -= price[1] * quantity
            quantity -= subtractions;
            subTotal += price[1] * quantity;
            print("Subtotal: ", subTotal)
    elif choice == 'H':
      print(" How many would you like to buy? ")
      quantity = int(input())
      subTotal += price[2] * quantity
      print("Subtotal: ", subTotal)
      print("Do you want to add these to the cart? (y/n) ")
      cart = (input())
      if cart == 'y':
        subTotal = subTotal
      else:
        print("Adding items? (y/n) ")
        edit = (input())
        if edit == 'y':
          print("How many? ")
          additions = int(input())
          subTotal -= price[2] * quantity
          quantity += additions
          subTotal += price[2] * quantity
          print("Subtotal: ", subTotal)
        else:
          print("Removing items? (y/n) ")
          edit = (input())
          print("How many? ")
          if edit == 'y':
            subtractions = int(input())
            subTotal -= price[2] * quantity
            quantity -= subtractions
            subTotal += price[2] * quantity
            print("Subtotal: ", subTotal)
    elif choice == 'M':
      print(" How many would you like to buy? ")
      quantity = int(input())
      subTotal += price[3] * quantity
      print("Subtotal: ", subTotal)
      print("Do you want to add these to the cart? (y/n) ")
      cart = (input())
      if cart == 'y':
        subTotal = subTotal
      else:
        print("Adding items? (y/n) ")
        edit = (input())
        if edit == 'y':
          print("How many? ")
          additions = int(input())
          subTotal -= price[3] * quantity
          quantity += additions
          subTotal += price[3] * quantity
          print("Subtotal: ", subTotal)
        else:
          print("Removing items? (y/n) ")
          edit = (input())
          if edit == 'y':
            print("How many? ")
            subtractions = int(input())
            subTotal -= price[3] * quantity
            quantity -= subtractions
            subTotal += price[3] * quantity
            print("Subtotal: ", subTotal)
    elif choice == 'F':
      print(" How many would you like to buy? ")
      quantity = int(input())
      subTotal += price[4] * quantity
      print("Subtotal: ", subTotal)
      print("Do you want to add these to the cart? (y/n) ")
      cart = (input())
      if cart == 'y':
        subTotal = subTotal
      else:
        print("Adding items? (y/n) ")
        edit = (input())
        if edit == 'y':
          print("How many? ")
          additions = int(input())
          subTotal -= price[4] * quantity
          quantity += additions
          subTotal += price[4] * quantity
          print("Subtotal: ", subTotal)
        else:
          print("Removing items? (y/n) ")
          edit = (input())
          if edit == 'y':
            print("How many? ")
            subtractions = int(input())
            subTotal -= price[4] * quantity
            quantity -= subtractions
            subTotal += price[4] * quantity
            print("Subtotal: ", subTotal)
    elif choice == 'X':
      total = subTotal
      print(" Your Total is ", total)
   