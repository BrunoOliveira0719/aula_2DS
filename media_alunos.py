condition = True 

notes = []

def verificator(notes):
    if notes == 0:
        print('Nota do aluno não pode ser zero! ')
    
    media = sum(notes) / len(notes)

    if media >= 7:
        response = f'Aprovado! \nA média é {media}'

    else:
        response = f'Aprovado! \nA média é {media}'

    return response

while condition:
    try:
        note = int(input('Digite uma nota: \n'))
        notes.append(note)
    except Exception as e:
        print(f'Entrada inválida! \nErro: \n{e}')

    choice = input('Deseja continuar? s/n: ').strip().lower()

    if choice in ['s', 'sim']:
        condition = True
    elif choice in ['n', 'não']:
        condition = False
    else:
        print('Opção inválida!')

print(verificator(notes))