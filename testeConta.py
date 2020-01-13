from conta import Conta, Data
conta = Conta(111, 'math', 5000.0, 100000.0)
conta2 = Conta(112, 'robert', 50.0, 10000.0)
conta.extrato()
conta.deposita(250)
conta.extrato()
# sacou 4000 reais da conta 1
conta.sacar(4000)
conta.extrato()
# tranferiu para conta 2 10 reais
conta.transferir(10, conta2)
conta2.extrato()
conta.extrato()
data = Data(31, 10, 2019)
data.formatacao()
print(conta.get_saldo())
print(conta.limite)
print(conta.get_titular())
conta.limite = 350.0
print(conta.limite)
conta.set_aumentar_limite(350.55)
print(conta.limite)
# conta2 possui 60 reais com calculos acima
conta2.sacar(10000)
conta2.extrato()
conta2.sacar(80)
# chamando metodos estaticos
print(Conta.codigo_banco())
print(Conta.codigos_bancos())
codigo_caixa = Conta.codigos_bancos()
print(codigo_caixa['Caixa'])
