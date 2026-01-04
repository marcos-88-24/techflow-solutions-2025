import os

estoque = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('presione ENTRE para continuar...')    

def mostrar_produtos():
        contador = 1
        for item in estoque:
            print (f'{contador} - {item}')
            contador += 1    

def selecionar_menu(opcao):
    if (opcao == '1'):
        nome_do_produto = input('Digite o nome do produto: ')
        preço_do_produto = float(input('Digite o preço do produto: '))
        quantidade_em_estoque = input('Digite quantidade em estoque: ')
        produto = {"Nome": nome_do_produto, "Preço": preço_do_produto, "Quantidade em estoque": quantidade_em_estoque}
        estoque.append(produto)



        
    elif (opcao == '2'):
        mostrar_produtos()
        numero_produto = int(input('Digite o número do produto para editar: '))
        nome_do_produto = input ('Alterar o nome do produto: ')
        preço_do_produto = float(input('Alterar o preço do produto: '))
        quantidade_em_estoque = input('Alterar a quantidade em estoque: ')
        novo_produto = {"Nome": nome_do_produto, "Preco": preço_do_produto, "Quantidade em estoque": quantidade_em_estoque}
        estoque[numero_produto -1] = novo_produto




        
    elif (opcao == '3'):
        mostrar_produtos()
        numero_produto = int(input ('Digitar o número produto para excluir: '))
        del estoque[numero_produto -1]       