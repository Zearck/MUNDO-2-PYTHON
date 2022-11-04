from random import randint
from time import sleep
computador = randint(0, 10)  # não tem problema colocar o número encima -> 10
print('Olá, eu sou o computador... Pensei em um número entre 0 e 10.')
sleep(3)
print('Você consegue adivinhar qual foi o que eu pensei? ')
sleep(3)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual será o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
