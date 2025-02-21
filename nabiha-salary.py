print ("Hello Nabiha\n")

salary = int(input("Please enter your Salary:\n"))

months = ["January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"]

month = input("Please enter the month of this salary in numbers (1-->12):\n")

while month == "" or int(month) > 12 or int(month) < 1:
    month = input("Enter a valid month number (1-->12):\n")

month = months[int(month) - 1]

finances = ["Savings", "Rent", "Electricity"]

percentages = []

for i in range(len(finances)):
    percentage = int(input("Enter the percentage for " + finances[i] +"\n"))

    percentages.append(percentage)

for i in range(len(percentages)):
    result = percentages[i] * salary / 100
    print("The amount allocated to " + str(finances[i]) + " in " + str(month) + " is: " + str(result) + " $\n")

total = sum(percentages) * salary / 100

print("The total spending in " + str(month) + " is: " + str(total) + " $\n")

remainder = salary - total

print("The remainder for "+ str(month) + " is: " + str(remainder) + " $\n")