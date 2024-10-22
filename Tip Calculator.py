print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
tip = tip / 100
totalprice = (bill * tip) + bill
people = int(input("How many people to split the bill? "))
finalsplit = round((totalprice/people), 2)
print(f"Each person should pay ${finalsplit}")