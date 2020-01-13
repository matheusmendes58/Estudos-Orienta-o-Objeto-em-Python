class Progama:  # classe mãe ou superclasse
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    def dar_like(self):
        self.__likes = self.__likes + 1
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def __str__(self):  # representação de String de objetos em python não é necessariamente obrigado a por desta forma
       return '{} - {} - {} '.format(self.nome, self.ano, self.likes)

class Filme(Progama): # herança em OO a classe mãe no caso ou superclasse é Progama feito no começo la em cima
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return '{} - {} - {} min - {} '.format(self.nome, self.ano, self.duracao, self.likes)

class Series(Progama):  # classe filha (classe filme tb é filha) que herda da classe mãe Progama
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return '{} - {} - {} temporadas - {} '.format(self.nome, self.ano, self.temporadas, self.likes)

class Playlist:
    def __init__(self, nome, progamas):
        self.nome = nome
        self.__programas = progamas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def listagem(self):
        return self.__programas

    def __len__(self):
        return len(self.__programas)

# criando objetos
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('todo mundo em panico', 1999, 100)
vingadores.dar_like()
print(vingadores.nome, vingadores.likes)

atantla = Series('atlanta', 2019, 2)
demolidor = Series('demolidor', 2016, 4)
atantla.dar_like()
atantla.dar_like()
atantla.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
print('nome: {} - ano: {} - temporadas: {} - likes: {}'.format(atantla.nome, atantla.ano, atantla.temporadas, atantla.likes))
'''  
lista ou arrays
filmes_e_series = [vingadores, atantla]
for progama in filmes_e_series:
    
    verificando objeto progama se possui duração com este if se tiver retorna duração 
    da serie atlanta se não o retorno sera quantidade de temporadas 
    função hasttr verifica se o obejto possui tal atributo como exemplo abaixo
    
    if hasattr(progama, 'duracao'):
        detalhes = progama.duracao
    else:
        detalhes = progama.temporadas
    print('{}'
          '\ndetalhes {}'
          '\n{}'.format(progama.nome, detalhes, progama.likes))
'''
filmes_e_series = [vingadores, tmep, atantla, demolidor]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print('tamanho do playlist {} '.format(len(playlist_fim_de_semana)))

for progama in playlist_fim_de_semana:
    '''
    resolvendo o problema acima dos ifs para não utilizar mais ifs 
    ou seja tenhamos que mecher na classe acima classe mãe para herdar metedo geral 
    e classe filha fazendo uma sobreescrita para metedos mais especificos mediante os atributos
    '''
    print(progama)