# ESTRUTURAS COM FOR

'''for variavel in range(10):
    print(variavel)'''


'''for variavel in range(5, 11):
    print(variavel)'''

# o terceiro parâmetro indica a distância dos números 'pular' de 2 em 2, 3 em 3...   
'''for variavel in range(1, 12, 3):
    print(variavel)
'''

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print(soma / 3)