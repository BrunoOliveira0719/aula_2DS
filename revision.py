operados_relacionais = ['<', '>', '==', '!=', '<=', '>=']
operados_logicos = ['and', 'or', 'not']
operadores_condicionais = ['if', 'elif', 'else', 'match case', 'try except']
lacos_de_repeticao = ['for', 'while']
funcoes_nativas = {'Funções básicas': '',
                   'print()': 'imprime uma informação',
                   'str()': 'Transforma uma váriavel em string',
                   'int()': 'Transforma uma váriavel em int',
                   'float()': 'Transforma um número em ponto flutuante(com casa decimal)',
                   'len()': 'Devolve a quantidade de indices de uma str ou list',
                   'sum()': 'Soma todos elementos de uma lista',
                   'max()': 'Maior elemento de uma lista',
                   'min()': 'Menor elemento de uma lista',
                   'upper()': 'Deixa toda a str maiúscula',
                   'lower()': 'Deixa toda a str minúscula',
                   } 
criar_funcoes = 'def'
criar_variavel = {'Tipos de variáveis': '',
                  'String': 'Tudo dentro de aspas',
                  'Int': 'Números inteiros',
                  'Float': 'Números com casas decimais',
                  'Bool': 'Verdadeiro ou Falso | True ou False',
                  'List': 'Uma lista de elementos: Podendo ter uma ou mais dimenções',
                  'Dict': 'Um dicionário',
                  'Para criar uma variável atribua um nome e use o sinal de =': 'idade = 17'}

class Interface:
    def user_order_discount(self):
        print('Bem vindo a calculadora de desconto!')

        price = float(input('Digite o preço: '))
        discount = float(input('Digite o desconto(SEM %): '))

        return price, discount
    
    def user_order_distance(self):
        print('Bem vindo a calculadora de horas gastas!')
        
        distance = float(input('Digite a distância percorrida: '))
        speed = float(input('Digite a velôcidade média: '))
        
        return distance, speed

    def user_order_energy(self):
        print('Bem vindo a calculadora de preço da energia!')
        
        kwh = float(input('Digite a quantidade de kWh(sem o kWh): '))
        classification = input('Digite R(residencial), I(industria), C(comercial): ').upper()
        
        return kwh, classification

class Calculetor():
    def discount(self, price, discount):
        try:
            result = price - ((price * discount)/100)

            return result
            
        except Exception as e:
            print(f'Error: \n{e}')

    def hours(self, distance, speed):
        try:
            result = distance / speed

            return result
            
        except Exception as e:
            print(f'Error: \n{e}')
    
    def kwh(self, kwh, classification):
        try:
            if classification == "R":
                if kwh <= 500: 
                    price = 0.4
                else:
                    price = 0.65
            elif classification == "C":
                if kwh <= 1000: 
                    price = 0.55
                else:
                    price = 0.6
            elif classification == "I":
                if kwh <= 5000: 
                    price = 0.55
                else:
                    price = 0.6

            result = kwh * price

            return result
        
        except Exception as e:
            print(f'Error: \n{e}')

interetion = Interface()
c = Calculetor()

kwh, classification = interetion.user_order_energy()
result = c.kwh(kwh, classification)

print(result)

