import pytest


class ObjDct:
    def __init__(self, dct):
        self._dct = dct

    def __getattr__(self, item):
        if item in self._dct:
            return self._dct[item]


def to_obj(dct):
    return ObjDct(dct)

@pytest.mark.parametrize(
    'dct',
    [{'a':1},
     {'a':1, 'b':2},
     {'a':1, 'b':2, 'c':3}
     ]
)

def test_acesso_atributos(dct):
    obj = to_obj(dct)
    for chave, valor in dct.items():
        assert valor == getattr(obj, chave, None)