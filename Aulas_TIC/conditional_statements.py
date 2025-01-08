#Python conditional statements exercises (from geeksforgeeks.org)

#Mark even and odd
#O objetivo do exercício é escrever um código para classificar como par ou ímpar
#um número fornecido pelo usuário

#Solução 1: Ajustando para pedir o número dentro da função
'''
def checkOddEven():
    numero = int(input("Digite o número a ser avaliado: "))
    if numero % 2 == 0:
        print("o número é par")
    else:
        print("o número é ímpar")

checkOddEven()
'''

#Solução 2: Ajustando para receber o número como parâmetro :

def checkOddEven(numero):
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

numero_usuario = int(input("digite o número a avaliar: "))

checkOddEven(numero_usuario)