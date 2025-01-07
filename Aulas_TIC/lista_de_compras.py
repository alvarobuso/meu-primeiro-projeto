''''def lista_de_compras():
    while True:
        print("Lista de Compras Simples")
        print()
        print("A. Adicionar produto")
        print("B. Remover produto")
        print("C. Pesquisar produtos")
        print("D. Sair do programa")
        opcao = input("Selecione uma opção: ")

       if opcao == 'D' or opcao == 'd':
            print("Obrigado por utilizar a Lista de Compras Simples")
            break

        if opcao not in ['A', 'B', 'C']:
            print("OPÇÃO INVÁLIDA")
            continue
'''''

def mostrar_cabecalho():
    print("=" * 40)
    print(" Bem-vindo à Lista de Compras Simples ")
    print("=" * 40)

def mostrar_menu():
    print("\nMENU DE OPÇÕES:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair do programa")

def listar_produtos(lista):
    if not lista:
        print("\nA lista de compras está vazia.")
    else:
        print("\nProdutos na lista de compras:")
        print("ID | Nome | Quantidade | Unidade | Descrição")
        print("-" * 40)
        for produto in lista:
            print(f"{produto['id']} | {produto['nome']} | {produto['quantidade']} | {produto['unidade']} | {produto['descricao']}")

def adicionar_produto(lista, contador_id):
    nome = input("\nDigite o nome do produto: ").strip()
    quantidade = input("Digite a quantidade: ").strip()
    print("Selecione a unidade de medida:")
    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    for i, unidade in enumerate(unidades, start=1):
        print(f"{i}. {unidade}")
    try:
        opcao_unidade = int(input("Escolha a unidade (número): "))
        unidade = unidades[opcao_unidade - 1]
    except (ValueError, IndexError):
        print("Opção inválida! Produto não foi adicionado.")
        return contador_id
    descricao = input("Digite a descrição do produto: ").strip()

    produto = {
        "id": contador_id,
        "nome": nome,
        "quantidade": quantidade,
        "unidade": unidade,
        "descricao": descricao
    }
    lista.append(produto)
    print(f"\nProduto '{nome}' adicionado com sucesso!")
    return contador_id + 1

def remover_produto(lista):
    try:
        id_remover = int(input("\nDigite o ID do produto que deseja remover: "))
        for produto in lista:
            if produto['id'] == id_remover:
                lista.remove(produto)
                print(f"Produto '{produto['nome']}' removido com sucesso!")
                return
        print("Produto com o ID informado não foi encontrado.")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar um número.")

def pesquisar_produtos(lista):
    termo = input("\nDigite o nome ou parte do nome do produto para pesquisar: ").strip().lower()
    resultados = [produto for produto in lista if termo in produto['nome'].lower()]

    if not resultados:
        print("\nNenhum produto encontrado.")
    else:
        print("\nProdutos encontrados:")
        print("ID | Nome | Quantidade | Unidade | Descrição")
        print("-" * 40)
        for produto in resultados:
            print(f"{produto['id']} | {produto['nome']} | {produto['quantidade']} | {produto['unidade']} | {produto['descricao']}")
        print(f"\nTotal de produtos encontrados: {len(resultados)}")

def main():
    lista_compras = []
    contador_id = 1

    mostrar_cabecalho()

    while True:
        listar_produtos(lista_compras)
        mostrar_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 1:
                contador_id = adicionar_produto(lista_compras, contador_id)
            elif opcao == 2:
                remover_produto(lista_compras)
            elif opcao == 3:
                pesquisar_produtos(lista_compras)
            elif opcao == 4:
                print("\nEncerrando o programa. Até mais!")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()