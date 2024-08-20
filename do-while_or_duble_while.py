while True:
    nums = [1]
    number_input = int(input('Digite um número para adicionar a lista: '))

    nums.append(number_input)

    if number_input != int:
        condition = True

    else:    
        print('Digite um número! ')
        condition = False
        
    while condition == True:
        print(sum(nums))
        break
    