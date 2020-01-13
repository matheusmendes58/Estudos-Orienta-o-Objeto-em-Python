# Herança multipla

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(('Horas registradas...'))

    def mostrar_tarefas(self):
        print('Fez muita coisa')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, CAELUMER')

    def buscar_curso_mes(self, mes=None):
        print('mostrando curso - {}'.format(mes) if mes else 'mostrando curso mes')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa alurete')

    def buscar_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return 'Hispster, {}'.format(self.nome)

# junior herda de alura e pleno herda de alura e caelum e alura e caelum herda de funcionario
class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior('josé')   # foi passado parametros só para nao apresentar erro ou seja por causa do construtor nome em funcionario
jose.buscar_perguntas_sem_respostas()
jose.mostrar_tarefas()
print('--------')
luan = Pleno('luan')    # foi passado parametros só para nao apresentar erro ou seja por causa do construtor nome em funcionario
luan.buscar_perguntas_sem_respostas()
luan.buscar_curso_mes()
luan.mostrar_tarefas()
# mixins
math = Senior('MATH')
print(math)


