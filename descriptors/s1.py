from collections import namedtuple

import pytest


class ItemPedido:

    def __init__(self, descricao, preco, quantidade):
        self.quantidade = quantidade
        self.descricao = descricao
        self.preco = preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor<=0:
            raise TypeError('Quantidade dever ser positiva')

        self._quantidade = valor


    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('ervilha', 1.21, 2)
    assert pytest.approx(2.42, item.subtotal())

def test_subtotal_negativo():
    item = ItemPedido('ervilha', 1.21, -2)
    with pytest.raises(TypeError):
        assert pytest.approx(-2.42, item.subtotal())

