class Cliente:
    _nome = None
    _cpf = None
    _profissao = None

    @property
    def nome(self) -> str:
        return Cliente._nome

    @nome.setter
    def nome(self, novonome):
        Cliente._nome = novonome

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, novocpf):
        self._nome = novocpf

    @property
    def profissao(self) -> str:
        return self._profissao

    @profissao.setter
    def profissao(self, novaprofissao):
        self._profissao = novaprofissao