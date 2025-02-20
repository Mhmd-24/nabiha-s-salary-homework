print ("Hello Nabiha\n")

salary = int(input("Please enter your Salary:\n"))

month = input("Please enter the month of this salary:\n")

finances = ["Savings", "Rent", "Electricity"]

percentages = []

for i in range(len(finances)):
    percentage = int(input("Enter the percentage for " + finances[i] +"\n"))

    percentages.append(percentage)

for i in range(len(percentages)):
    result = percentages[i] * salary / 100
    print("The amount allocated to " + str(finances[i]) + " is: " + str(result) + " $\n")

total = sum(percentages) * salary / 100

print("The total spending is: " + str(total) + " $\n")

remainder = salary - total

print("The remainder is: " + str(remainder) + " $\n")