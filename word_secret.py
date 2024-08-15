import requests
import random
import os

new_attempt = True

while new_attempt == True:
    try:
        print('Bem-vindo ao jogo para encontrar palavras: \n')

        print('Vamos encontrar uma palavra secreta! \n')

        print('Qual dificuldade você deseja? \n')
        print('1 para fácil \n2 para médio \n3 para difícil \n')

        def get_random_word():
            url = "https://api.dicionario-aberto.net/random"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                palavra = data['word']
                return palavra
            else:
                return None

        word = get_random_word()

        def code_word():
            amount_character = len(word)
            coded_word = ['*'] * amount_character
            return coded_word

        numbers_attempts = 0

        choice = int(input('Digite o número da dificuldade: '))

        if choice == 1:
            numbers_attempts = int(input('Escolha a quantidade de tentativas: '))
        elif choice == 2:
            numbers_attempts = 2
        elif choice == 3:
            numbers_attempts = 1
        else:
            print('Dificuldade inválida')

        numbers_attempts = numbers_attempts * len(word)
        coded_word = code_word()

        for c in range(numbers_attempts):
            print(''.join(coded_word))
            letter = str(input('Digite uma letra: ').lower())
            
            if letter and len(letter) == 1:
                for l in range(len(word)):
                    if letter == word[l]:
                        coded_word[l] = word[l]

                if '*' not in coded_word:
                    print('Parabéns! Você descobriu a palavra!')
                    new_attempt = str(input('Quer jogar outra vez? S/N \n').lower())
                    continue

                attempts_remaining = (numbers_attempts - 1) - c
                print(f'Você tem {attempts_remaining} tentativas restantes.')

            else:
                print('Por favor, digite uma única letra válida.')

        if '*' in coded_word:
            print(f'Você perdeu! A palavra secreta era: {word} \n')
            new_attempt = str(input('Quer tentar outra vez? S/N \n').lower())
            continue

        if new_attempt == 's' or new_attempt == 'sim':
            os.system('cls')
            attempt = True
        elif new_attempt == 'n' or new_attempt == 'não':
            os.system('cls')
            attempt = False
        else:
            os.system('cls')
            print('Por favor, digite S ou N')
        
    except Exception as e:
        print(f'Erro: \n{e}')