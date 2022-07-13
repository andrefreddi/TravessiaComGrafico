import pygame
import random
import copy
import time
from os import system, name

# Lugar de cada peragem.
PAI = 0
MAE = 1
FILHO_1 = 2
FILHO_2 = 3
FILHA_1 = 4
FILHA_2 = 5
LADRAO = 6
POLICIAL = 7
BARCO = 8

#pygames
pygame.init()
TelaWin = pygame.display.set_mode((650, 650))
FonteLetra = pygame.font.SysFont('Arial', 20)
pessoa = []
D = 300

# Estado inicial, no lado esquerdo, compondo todos os itens (pessoas e o Barco)
# E = Esquerdo
START_STATE = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
# Definido as regras usada para o ladrao

class Person():
    def __init__(self, name, x, y, color, side='UP', w=20, h=20, hate=[], like=[], alone=None):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.alone = alone
        self.hate = hate
        self.like = like
        self.side = side
        self.obj = pygame.Rect(x, y, w, h)
        pessoa.append(self)
        conditions = []
        self.conditions = conditions

    def resetaPosicao(self,x,y):
        pessoa.pop(self)

    def Empate(self):
        self.obj = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(TelaWin, self.color, self.obj)

    def condicoesgravacao(self, x, y):
        text = FonteLetra.render(f"{self.name} {'; '.join(self.conditions)}", True, (0, 0, 0))
        TelaWin.blit(text, (x, y))


class PosicaoInicial():
    def __init__(self, room, x=280, y=200,):
        self.x = x
        self.y = y



def RegraLadrao(state):
    return state[POLICIAL] == state[LADRAO] or (
        state[LADRAO] != state[PAI]
        and state[LADRAO] != state[MAE]
        and state[LADRAO] != state[FILHO_1]
        and state[LADRAO] != state[FILHO_2]
        and state[LADRAO] != state[FILHA_1]
        and state[LADRAO] != state[FILHA_2]
    )


# Definido as regras usada para a filha
def RegraFilha(state):
    return (
        state[FILHA_1] == state[MAE] or state[FILHA_1] != state[PAI]
    ) and (state[FILHA_2] == state[MAE] or state[FILHA_2] != state[PAI])


# Definido as regras usada para o filho
def RegraFilho(state):
    return (state[FILHO_1] == state[PAI] or state[FILHO_1] != state[MAE]) and (
        state[FILHO_2] == state[PAI] or state[FILHO_2] != state[MAE]
    )


# Verifica se as regras estao validas, verifica as 3 regras definidias a cima
def ValidaRegras(state):
    return RegraLadrao(state) and RegraFilha(state) and RegraFilho(state)


# Estado final esperado no lado direito, com todos os membros (pessoas e o bote)
# D = Direita
def Objetivo(state):
    return state == ["D", "D", "D", "D", "D", "D", "D", "D", "D"]


# Agora vamos gerar todos os possiveis movimentos
def GerarMovimentos(state):
    for other in [PAI, MAE, FILHA_1, FILHA_2, FILHO_1, FILHO_2, LADRAO, POLICIAL]:

        if state[PAI] == state[other] == state[BARCO]:
            move = copy.deepcopy(state)
            move[PAI] = "E" if state[PAI] == "D" else "D"
            move[other] = "E" if state[other] == "D" else "D"
            move[BARCO] = "E" if state[BARCO] == "D" else "D"
            yield move

        if state[MAE] == state[other] == state[BARCO]:
            move = copy.deepcopy(state)
            move[MAE] = "E" if state[MAE] == "D" else "D"
            move[other] = "E" if state[other] == "D" else "D"
            move[BARCO] = "E" if state[BARCO] == "D" else "D"
            yield move

        if state[POLICIAL] == state[other] == state[BARCO]:
            move = copy.deepcopy(state)
            move[POLICIAL] = "E" if state[POLICIAL] == "D" else "D"
            move[other] = "E" if state[other] == "D" else "D"
            move[BARCO] = "E" if state[BARCO] == "D" else "D"
            yield move

# Filtrar apenas os movimentos válidos
def ValidarMovimentos(state_list):
    validList = []
    for state in state_list:
        if ValidaRegras(state) and state not in validList:
            validList.append(state)
    return validList
    


# Faz uma pesquisa limitada, usando uma lista previous_states para acompanhar onde estivemos. Esta função retorna apenas uma resposta vencedora.
def Pesquisalimitada(state, previous_states, maxDepth):
    previous_states.append(state)

    if Objetivo(state):
        return previous_states

    if maxDepth <= 0:
        return None

    for move in ValidarMovimentos(GerarMovimentos(state)):
        if move not in previous_states:
            result = Pesquisalimitada(move, previous_states, maxDepth - 1)
            if result is not None:
                return result
            previous_states.pop()

    return None

# Imprimir o estado atual no terminal
def Exibir(state_list):

    Posicao = PosicaoInicial(2)

    for l in range(len (state_list)) :

        if l == state_list[-1]:
            Person.resetaPosicao(Posicao.x+0, Posicao.y)
        
        Pai = state_list[l]
        if Pai == 'E':
            Pai = Person('Pai', Posicao.x+0, Posicao.y, (39, 243, 243))
        else:
            Pai = Person('Pai', Posicao.x, Posicao.y+300, (39, 243, 243))

        Mae = state_list[l]  
        if Mae == 'E':
            Mae = Person('Mae', Posicao.x+30, Posicao.y, (243, 39, 114))
        else:
            Mae = Person('Mae', Posicao.x+30, Posicao.y+300, (243, 39, 114))

        Filha01 = state_list[l]  
        if Filha01 == 'E':
            Filha01 = Person('Filha01', Posicao.x+60, Posicao.y, (255, 0, 255))
        else:
            Filha01 = Person('Filha01', Posicao.x+60, Posicao.y+300, (255, 0, 255))

        Filha02 = state_list[l]  
        if Filha02 == 'E':
            Filha02 = Person('Filha02', Posicao.x+90, Posicao.y, (250, 102, 226)) 
        else:
            Filha02 = Person('Filha02', Posicao.x+90, Posicao.y+300, (250, 102, 226)) 

        Filho01 = state_list[l]  
        if Filho01 == 'E':
            Filho01 = Person('Filho01', Posicao.x+120, Posicao.y, (34, 0, 255)) 
        else:
            Filho01 = Person('Filho01', Posicao.x+120, Posicao.y+300, (34, 0, 255)) 

        Filho02 = state_list[l]  
        if Filho02 == 'E':
            Filho02 = Person('Filho02', Posicao.x+150, Posicao.y, (113, 91, 255))
        else:
            Filho02 = Person('Filho02', Posicao.x+150, Posicao.y+300, (113, 91, 255))

        Policial = state_list[l]  
        if Policial == 'E':
            Policial = Person('Policial', Posicao.x+180, Posicao.y, (255, 0, 0)) 
        else:
            Policial = Person('Policial', Posicao.x+180, Posicao.y+300, (255, 0, 0)) 

        Ladrao = state_list[l]  
        if Ladrao == 'E':
            Ladrao = Person('Ladrao', Posicao.x+210, Posicao.y, (0, 0, 0)) 
        else:
            Ladrao = Person('Ladrao', Posicao.x+210, Posicao.y+300, (0, 0, 0)) 

        

# Imprimir o caminho no terminal com a ajuda da função Exibir()
def ExecucaoAuto(state_list, delay):
    for state in state_list:
        Exibir(state)
        time.sleep(delay)
        system("cls")

# Função principal, execução automática
def main():

    state_list = Pesquisalimitada(
        ["E", "E", "E", "E", "E", "E", "E", "E", "E"], [], 30
    )

    print("Execução da resulução do problema:")

    


 

    ExecucaoAuto(state_list, 0.1)


#    Filha01 = Person('Filha01', Posicao.x+60, Posicao.y, (255, 0, 255)) 
#    Filha02 = Person('Filha02', Posicao.x+90, Posicao.y, (250, 102, 226)) 
#    Filho01 = Person('Filho01', Posicao.x+120, Posicao.y, (34, 0, 255)) 
#    Filho02 = Person('Filho02', Posicao.x+150, Posicao.y, (113, 91, 255))
#    Policial = Person('Policial', Posicao.x+180, Posicao.y, (255, 0, 0)) 
#    Ladrao = Person('Ladrao', Posicao.x+210, Posicao.y, (0, 0, 0)) 
    print(state_list)

main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

                
    TelaWin.fill((255, 255, 255))
    pygame.draw.rect(TelaWin, (100, 200, 255), (0, 290, 650, 180))
    

    for i, person in enumerate(pessoa):
        person.Empate()
        person.condicoesgravacao(0, i*25)


    pygame.display.update()