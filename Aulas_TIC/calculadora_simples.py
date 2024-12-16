
def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("S. Sair")
        operacao = input("Selecione uma opção: ")

        if operacao == 's' or operacao == 'S':
            print ("Obrigado por utilizar a Calculadora Simples")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("OPÇÃO INVÁLIDA")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação de soma é ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação de subtração é ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação de multiplicação é ", resultado)

        else:
            if numero_2 == 0:
                print("Divisões por zero não existem!")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da operação de divisão é ", resultado)

calculadora()