rotas = {}

class RotaInexistente(Exception):
    def erro(self):
        raise TypeError

def rota(url):
    def decorator(func):
        rotas[url] = func
        return func

    return decorator

def rotear(url, *args, **kwargs):
    if url in rotas:
        return rotas[url](*args, **kwargs)
    else:
        raise RotaInexistente(f'Rota inexistente: {url}')

@rota('/')
def home():
    def home_url():
        return 'home executada'

    return home_url

@rota('/carro')
def carro():
    def carro_rota(*args, **kwargs):
        if 'nome' and 'ano' in kwargs:
            return f'{kwargs["nome"]} ano {kwargs["ano"]}'
        elif args is not None:
            nome = args[0]
            ano = args[1]
            return f'{nome} ano {ano}'

    return carro_rota

@rota('/usuario')
def usuario():
    def usuario_rota(nome):
        return f'salvando {nome}'

    return usuario_rota
