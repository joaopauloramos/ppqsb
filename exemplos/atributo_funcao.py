nome = 'JOAO'

def f(a: int, b:int=2,*,c:str ='3') -> str:
    """Funcao exemplo para verificar atributos"""
    print(nome)

f.parametro = True
if __name__ == '__main__':
    print(f.__doc__)
    print(f.__defaults__)
    print(f.__globals__)
    print(f.__dict__)
    print(f.__closure__)
    print(f.__annotations__)
    f(a=1, b=2, c=3)
    print(f.__kwdefaults__)