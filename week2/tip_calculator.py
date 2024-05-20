
bill_amount = float(input("Input bill amount: "))

tip_percentage = float(input("Input tip percentage: "))

total_amount = bill_amount + bill_amount * (tip_percentage / 100)

print(f"The total amount to pay is {total_amount}")