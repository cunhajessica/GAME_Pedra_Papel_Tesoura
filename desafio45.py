from random import randint
from time import sleep
print('*-*' *7)
print('Vamos jogar Pedra, Papel, Tesoura?')
print('*-*' *7)
print('''Suas opções são:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
op = int(input('Qual é a sua opção?'))
comp = randint(1, 3) # faz o computador pensar
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
if comp == 1 and op == 1:
    print('Eu escolhi 1.')
    print('PEDRA e PEDRA, ninguém ganhou! Vamos de novo!')
elif comp == 2 and op == 2:
    print('Eu escolhi 2.')
    print('PAPEL e PAPEL, ninguém ganhou! Vamos de novo!')
elif comp == 3 and op == 3:
    print('Eu escolhi 3.')
    print('TESOURA e TESOURA, ninguem ganhou! Vamos de novo!')
elif comp == 1 and op == 2:
    print('Eu escolhi 1.')
    print('O PAPEL ganha da PEDRA! Você venceu!')
elif comp == 2 and op == 1:
    print('Eu escolhi 2.')
    print('O PAPEL ganha da PEDRA! Eu venci!')
elif comp == 1 and op == 3:
    print('Eu escolhi 1.')
    print('A PEDRA ganha da TESOURA! Eu venci!')
elif comp == 3 and op == 1:
    print('Eu escolhi 3.')
    print('A PEDRA ganha da TESOURA! Você venceu!')
elif comp == 2 and op == 3:
    print('Eu escolhi 2.')
    print('A TESOURA ganha do PAPEL! Você venceu!')
elif comp == 3 and op == 2:
    print('Eu escolhi 3.')
    print('A TESOURA ganha do PAPEL! Eu venci!')






