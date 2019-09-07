#Cada numero esta relacionado
    #3 propriedades binarias
        #Paridade
        #Cor
        # 1 <= n <= 18 ou nao
    #2 propriedades ternarias
        #Primeiros 12, Segundos 12, Terceiros 12
        #Primeira coluna, Segunda coluna, Terceira coluna
    #A excecao de tudo isso eh o zero (ou o 00, no caso da roleta americana)
        #Ele nao se associa a nenhuma categoria (paridade, cor,...)

#Como modelar essas informacoes
    #O que parece ser mais adequado e utilizar dicionarios
    #cada numero esta associado a um dicionario, esse dicionario contem as informacoes de cada numberOfPlayers
        #Se eh par ou impar, se eh preto ou branco, qual metade pertence,...

# exemplo = {
#     'id': 1,
#     'even': False,
#     'red': True,
#     'lessOrEqual18': True,
#     'firstTwelve': True,
#     'secondTwelve': False,
#     'thirdTwelve': False,
#     'firstColumn': True,
#     'secondColumn': False,
#     'thirdColumn': False,
# }
# if 0 in range(1,37,3):
#     print('Yes!')
# else:
#     print('No!')

class Mae:
    def __init__(self):
        self.teste = 'oi'
        # self.digaOi()
        self.digaOi()
    def oi(self):
        print('Oi')
        
    def digaOi(self):
        self.oi()
class Filho(Mae):
    def __init__(self):
        super().__init__()

filho = Filho()
