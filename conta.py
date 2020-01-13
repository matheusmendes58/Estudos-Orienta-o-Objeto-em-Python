class Conta:
    # função construtora de objetos
    def __init__(self, numero, titular, saldo, limite):
        print('construindo objetos... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # métodos
    def extrato(self):
        print('O saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo = self.__saldo - valor
        else:
            print('o valor {} passou o limite'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    # aprendendo getters e setters
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    '''   
    usando propiedades pega atributo limite e quando definir função nao é necessario
    usar get_limite exemplo abaixo de propiedades porém usar esse método em atributos privados
    @property pode ser usado para melhoramento de códido orientado objeto REFATORAÇÃO DE CÓDIGO
    '''
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    def set_aumentar_limite(self, limite):
        self.__limite = self.__limite + limite

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia

        self.mes = mes
        self.ano = ano

    def formatacao(self):
        print('{}/{}/{}'.format(self.dia, self.mes, self.ano))


