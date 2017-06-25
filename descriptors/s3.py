import pytest

class Quantidade:

        def __init__(self):
            self.nome = None

        def set_nome(self, nome):
            self._nome = f'_{nome}'

        def __get__(self, item, owner):
            return getattr(item, self._nome)

        def __set__(self, item, valor):
            if valor <= 0:
                raise TypeError('Quantidade deveria ser positiva')
            setattr(item, set._nome, valor)

class ItemPedido:
    quantidade = Quantidade()
    preco = Quantidade()

    def __new__(cls, *args, **kwargs):
        for nome, valor in cls.__dict__.items():
            print(nome, valor)

