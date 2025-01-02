print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size of choice. 
bill=0
if size == 'S':
    bill += 15
    print("Small size is $15")
elif size == 'M': 
    bill += 20
    print("Medium size is $20")
elif size == 'L':
    bill += 25
    print("Large size is $25")
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice. 
if pepperoni == 'Y': 
    bill += 2
    print("Pepperoni will add $2")

# todo: work out their final amount based on whether if they want extra cheese. 
if extra_cheese == 'Y': 
    bill +=1
    print("Extra cheese will add $1")

print(f"Your bill: {bill}")
