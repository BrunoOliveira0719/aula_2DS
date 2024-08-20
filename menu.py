def menu():
    print('Olá mundo; \nEu programo em Python; \nLaços de repetição.')

    while True:
        choice = int(input('Digite uma das três opções: (1/2/3)'))
        
        var = 0

        if choice == 1:
            var = 1
            print(f'Você digitou {var} que equivale há Olá mundo')

        elif choice == 2:
            var = 2
            print(f'Você digitou {var} que equivale há Eu programo em Python')

        elif choice == 3:
            var = 3
            print(f'Você digitou {var} que equivale há Laços de repetição')

        else:
            print('Opção inválida!!! \n')

            menu()

menu()