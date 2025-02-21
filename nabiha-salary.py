print ("Hello Nabiha\n")

salary = int(input("Please enter your Salary:\n"))

month = int(input("Please enter the month of this salary in numbers (1-->12):\n"))

while month > 12 or month < 1 :
    month = int(input("Enter a valid month number (1-->12):\n"))

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