#lista_de_compras = ["arroz", "feijão", "batata", "macarrão"]
#
#for produto in lista_de_compras:
#    print("Comprei o item", produto)

#numero = 0

#while True:
  #  print ("número", numero)
 #   numero = numero + 1
#
  #  if numero == 10:
 #       print("Meu número é 10")
#        break

numero = 0

while True:
    print ("número", numero)
    numero = numero + 1

    if numero % 2 == 0: #verifica se numero é par (resto da divisão = 0)
        print(numero, "é par")
        continue

    print(numero, "é ímpar")