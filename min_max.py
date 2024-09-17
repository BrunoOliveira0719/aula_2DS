numbers = []

for num in range(3):
    choice_number = float(input('Enter one number: '))
    numbers.append(choice_number)

print(f'The maxnimum number is {max(numbers)} and the minimum is {min(numbers)}')