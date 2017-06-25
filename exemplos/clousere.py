def criar_conta(saldo):

    def retirada(valor):
        nonlocal saldo
        if valor >= saldo:
            raise ValueError("Valor nao pode ser maior que o saldo")
        saldo -= valor
        return saldo

    return retirada


if __name__ == '__main__':
    retirar = criar_conta(400)
    print(retirar(250))