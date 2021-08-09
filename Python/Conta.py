from abc import abstractmethod
from Cliente import *


class Conta:
    _saldo = 0.0
    __agencia = 0
    __numero = 0
    __total = 0
    __titular_nome = Cliente.nome

    def __init__(self, numero, agencia):
        Conta.__total += 1
        self.__numero = numero
        self.__agencia = agencia

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, var):
        if var <= 0:
            print("Não pode numero menor igual a 0")
            return
        self.__numero = var

    @property
    def agencia(self) -> int:
        return self.__agencia

    @agencia.setter
    def agencia(self, var):
        if var <= 0:
            print("Não pode agencia menor igual a 0")
            return
        self.__agencia = var

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def titular_nome(self) -> str:
        return self.__titular_nome

    @titular_nome.setter
    def titular_nome(self, novotitular):
        self.__titular_nome = novotitular

    @staticmethod
    def get_total() -> int:
        return Conta.__total

    @abstractmethod
    def deposita(self, valor):
        return

    def saca(self, valor):
        if self._saldo < valor:
            raise Exception(f"Saldo total: {self._saldo}, Valor do saque: {valor}")
        else:
            self._saldo -= valor

    def transfere(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)

    def compara_saldo(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return -1 if outra._saldo < Conta._saldo else 1

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.__agencia == outra.__agencia and self.numero == outra.__numero

    @property
    def dados(self):
        return f" Numero {self.numero}, " \
               f"Agência {self.agencia}, Saldo: {self.saldo:.2f}"


class ContaPoupanca(Conta):

    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)

    def deposita(self, valor):
        ContaPoupanca._saldo += valor

    @property
    def dados(self) -> str:
        return f"Conta Poupanca: {super().dados}"

    def saca(self, valor):
        valorasacar = valor + 0.2
        super().saca(valorasacar)


class ContaCorrente(Conta):

    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)

    def deposita(self, valor):
        ContaCorrente._saldo += valor

    @property
    def dados(self) -> str:
        return f"Conta Corrente: {super().dados}"


if __name__ == "__main__":
    a = ContaCorrente(11, 22)
    b = ContaPoupanca(22, 33)

    a.deposita(200)
    b.deposita(500)

    print(a.dados)
    print(b.dados)

    a.transfere(100, b)

    print(a.dados)
    print(b.dados)

    a.saca(10)
    b.saca(500)

    print(a.dados)
    print(b.dados)

    print(Conta.compara_saldo(a, b))
