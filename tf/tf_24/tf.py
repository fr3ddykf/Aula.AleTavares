
def adicionar(estoque, nome, preco, quantidade):
    if nome in estoque:
        estoque[nome]['quantidade'] += quantidade
    else:
        estoque[nome]={'preco':preco, 'quantidade':quantidade}
def excluir(estoque,nome):
    if nome in estoque:
        del estoque[nome]
    else:
        print(f'o produto "{nome}" não esta no estoque.')
def lista (estoque):
    if estoque:
        print("Estoque")
        for nome, detalhes in estoque.items():
            print(f'Nome: {nome}, Preço : R${detalhes["preco"]:.2f}, Quantidade: {detalhes["quantidade"]}')
        else:
            print("inventario vazio")    
estoque={}

print(input("1.Adicionar produto\n2.Remover produto\n3.Listar Produtos\n"))
opcao= input
if opcao== '1':
    nome=input("digite o nome do produto:\n")
    preco=input("digite o valor:\n")
    quantidade=input("digite a quantidade:\n")
    adicionar(estoque,nome,preco,quantidade)
elif opcao == '2':
    nome=input("digite o nome do produto a ser removido:\n")
    excluir(estoque, nome)
elif opcao == '3':
    lista(estoque)  
else:
    print("opção invalida")
