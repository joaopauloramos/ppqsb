class Singlenton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance




class Invocavel:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self):
        return self.numero


if __name__ == '__main__':
    invocaveis = map(Invocavel, range(1,8))

    for invocavel in invocaveis:
        print(invocavel())


    singlenton_1 = Singlenton()
    singlenton_2 = Singlenton()
    print(id(singlenton_1), id(singlenton_2))
    print(singlenton_1 is singlenton_2)