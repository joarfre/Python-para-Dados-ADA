# ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

'''
    Imagine que você queira imprimir "Aprovada(o)",
    caso o estudante tenha uma média superior
    ou igual a 7, e "Reprovada(o)",
    caso a média seja inferior a 7.
'''
'''
media = float(input('Informe a média do estudante'))

if media >= 7:
    print('Aprovada(o)!')
elif media >= 5:
    print('Recuperação.')
else:
    print('Reprovada(o).')
'''

media = 5
presenca = 100
if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')