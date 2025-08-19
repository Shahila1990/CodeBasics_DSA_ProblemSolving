max_number = int(input("Enter your max limit : "))

odd_numbers = []

for i in range(1,max_number):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd Numbers :" , odd_numbers)