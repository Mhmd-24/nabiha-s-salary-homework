print ("Hello Nabiha\n")

salary = input("Please enter your Salary:\n")

while not salary.isdigit() or int(salary) <= 0:
    salary = input("Please enter a proper Salary:\n")


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = input("Please enter the month of this salary in numbers (1-->12):\n")

while not month.isdigit() or not (1 <= int(month) <= 12):
    month = input("Enter a valid month number (1-->12):\n")

month = months[int(month) - 1]

finances = ["Savings", "Rent", "Electricity"]

percentages = []

total_percentage = 0

for i in range(len(finances)):
    while True:
        percentage = input("Enter the percentage for " + str(finances[i]) + " :\n")
        if not percentage.isdigit() or int(percentage) < 0:
            print("Please enter a proper percentage (1-->100).\n")
        elif total_percentage + int(percentage) > 100:
            print("The total percentage exceeds 100%, please enter a lower value.\n")
        else:
            break
    percentages.append(int(percentage))
    total_percentage += int(percentage)

results = []

for i in range(len(percentages)):
    result = percentages[i] * int(salary) / 100
    print("The amount allocated to " + str(finances[i]) + " in " + str(month) + " is: $" + str(result) + "\n")
    results.append(result)

total = sum(percentages) * int(salary) / 100

print("The total spending in " + str(month) + " is: $" + str(total) + "\n")

remainder = int(salary) - total

print("The remainder for "+ str(month) + " is: $" + str(remainder) + "\n")

yearlyrent = (results[1] + results[2]) * 12

print("Nabiha's yearly rent and electricity costs is: $" + str(yearlyrent) + "\n")

powered = pow(int(salary), 2)

print("Nabiha's total salary for the month raised to the power of 2 (just for fun) is: $" + str(powered) + "\n")

answer = input("Is there additional savings? Y/N \n").strip().upper()

while answer not in ("Y", "N"):
    answer = input("Please enter Y or N \n").strip().upper()

if answer == "Y":
    if results[0] == 0:
        print("Total savings allocation is 0, so the division cannot be performed.")
    else:
        additional_savings = input("Please enter the value:\n") 
        while not additional_savings.isdigit():
            additional_savings = input("Please enter a proper value:\n") 
        ratio = int(additional_savings) / results[0]
        print("The additional savings divided by the total savings allocation is: " + str(ratio))
elif answer == "N":
    print("There's no additional savings, Good Bye.\n")