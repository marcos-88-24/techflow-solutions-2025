import unittest
from estoque_logica import (
    cadastrar_produto,
    atualizar_produto,
    excluir_produto
)

class TestEstoque(unittest.TestCase):

    def test_cadastrar_produto(self):
        estoque = []
        cadastrar_produto(estoque, "Arroz", 25.90, 10)

        self.assertEqual(len(estoque), 1)
        self.assertEqual(estoque[0]["Nome"], "Arroz")

    def test_atualizar_produto(self):
        estoque = [{"Nome": "Arroz", "Preço": 25.90, "Quantidade": 10}]
        resultado = atualizar_produto(estoque, 0, "Arroz Integral", 30.00, 5)

        self.assertTrue(resultado)
        self.assertEqual(estoque[0]["Preço"], 30.00)

    def test_excluir_produto(self):
        estoque = [{"Nome": "Arroz", "Preço": 25.90, "Quantidade": 10}]
        resultado = excluir_produto(estoque, 0)

        self.assertTrue(resultado)
        self.assertEqual(len(estoque), 0)

    def test_excluir_produto_invalido(self):
        estoque = []
        resultado = excluir_produto(estoque, 0)

        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
