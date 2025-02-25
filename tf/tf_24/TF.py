def adicionar_produto(inventario, nome, preco, quantidade):
    if nome in inventario:
        inventario[nome]['quantidade'] += quantidade
    else:
        inventario[nome] = {'preco': preco, 'quantidade': quantidade}

# Função para remover um produto do inventário
def remover_produto(inventario, nome):
    if nome in inventario:
        del inventario[nome]
    else:
        print(f'O produto "{nome}" não está no inventário.')

# Função para listar todos os produtos do inventário
def listar_produtos(inventario):
    if inventario:
        print("Inventário de produtos:")
        for nome, detalhes in inventario.items():
            print(f'Nome: {nome}, Preço: R${detalhes["preco"]:.2f}, Quantidade: {detalhes["quantidade"]}')
    else:
        print("O inventário está vazio.")

# Função principal
def main():
    inventario = {}
    while True:
        print("\nOpções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(inventario, nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto a remover: ")
            remover_produto(inventario, nome)
        elif opcao == '3':
            listar_produtos(inventario)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()