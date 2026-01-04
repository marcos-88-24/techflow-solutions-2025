
elif (opcao == '1'):
    nome_do_produto = input('Digite o nome do produto: ')
    preço_do_produto = float(input('Digite o preço do produto: '))
    quantidade_em_estoque = input('Digite quantidade em estoque: ')
    produto = {
        "Nome": nome_do_produto,
        "Preço": preço_do_produto,
        "Quantidade em estoque": quantidade_em_estoque
    }
    estoque.append(produto)
