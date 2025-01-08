#Uso de lista para guardar informações sobre uma pessoa:
'''''
pessoa = ["João", 25, "São Paulo"]
print(pessoa[2])
'''''

#Uso do dicionário para essa mesma finalidade (as informações ficam mais claras e organizadas
'''''
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print(pessoa["nome"])
'''''

#Crie um programa para armazenar informções de produtos em um dicionário, com as seguintes chaves:
# id
# nome
# preco

#Peça os dados ao usuário e exiba o dicionário no final

produto = {}
produto["id"] = input("Digite o ID do produto: ")
produto["nome"] = input("Digige o nome do produto: ")
produto["preco"] = input("Digite o preço do produto: ")

print("\nInformações do produto:")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")
