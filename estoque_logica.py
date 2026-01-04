def cadastrar_produto(estoque, nome, preco, quantidade):
    produto = {
        "Nome": nome,
        "Preço": preco,
        "Quantidade": quantidade
    }
    estoque.append(produto)
    return estoque


def atualizar_produto(estoque, indice, nome, preco, quantidade):
    if indice < 0 or indice >= len(estoque):
        return False

    estoque[indice] = {
        "Nome": nome,
        "Preço": preco,
        "Quantidade": quantidade
    }
    return True


def excluir_produto(estoque, indice):
    if indice < 0 or indice >= len(estoque):
        return False

    del estoque[indice]
    return True
