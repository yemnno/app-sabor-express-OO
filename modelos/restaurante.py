from modelos.avaliacao import Avaliacao

class Restaurante:

    '''Representa um restaurante e suas características.'''

    restaurantes = []

    def __init__(self, nome, categoria):

        '''
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''

        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):

        '''Retorna uma representação em string do restaurante.'''

        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        
        '''Retorna uma lista detalhada de cada restaurante.'''

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):

        '''Retorna um símbolo indicando o estado de atividade do restaurante.'''

        return '⊠' if self._ativo else '☐'      
    
    def alternar_estado(self):

        '''Alterna o estado de atividade do restaurante'''
        
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):

        '''
        Recebe a avaliação de um restaurante
           
        parâmetros:
        cliente(str): recebe o nome do cliente em valor de string.
        nota(float): recebe a nota do restaurante em um número de 1 a 5
        '''

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):

        '''
        Retorna o cálculo da média de notas do restaurante, buscando na lista de avaliações.
        Se não houver avaliações, retorna como 'não avaliado'
        '''

        if not self._avaliacao:
            return 'Não avaliado'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)     
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
