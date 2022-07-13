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

# Estado inicial, no lado esquerdo, compondo todos os itens (pessoas e o Barco)
# E = Esquerdo
START_STATE = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
# Definido as regras usada para o ladrao
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
def Exibir(state):
    CHARACTERSNAME = [
        "PAI",
        "MAE",
        "FILHO_1",
        "FILHO_2",
        "FILHA_1",
        "FILHA_2",
        "LADRAO",
        "POLICIAL",
    ]
    espaco = " " * 10
    texto = "| {} |                | {} |"

    print(" ")
    print(texto.format(espaco, espaco))

    for i in range(0, 8):
        characterName = CHARACTERSNAME[i] + " " * (10 - len(CHARACTERSNAME[i]))

        if state[i] == "E":
            print(texto.format(characterName, espaco))
        else:
            print(texto.format(espaco, characterName))

        if i == 3:
            if state[8] == "D":
                print("|", espaco, "|                |", espaco, "|")
            else:
                print("|", espaco, "|                |", espaco, "|")

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

    ExecucaoAuto(state_list, 1.5)

main()