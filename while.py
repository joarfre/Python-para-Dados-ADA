num_sorteado = 15

num_escolhido = int(input('Informe um número entre 1 e 20: '))

while num_escolhido != num_sorteado:
    print('Você errou o número, tente novamente...')

    num_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns! Você acertou!')

# EXEMPLO 2: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1