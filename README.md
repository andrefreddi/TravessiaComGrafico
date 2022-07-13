# Travessia Com Grafico
Desenvolvido por Andre Freddi e Willian Choaste

### Ideia:

A ideia inicial era juntar nosso algorítimo que realizava ao problema da travessia utilizando de um algorítimo para realizar a mesma e demonstrar de uma maneira bonita e dinâmica para o usuário. Utilizando da biblioteca [PyGames](https://www.pygame.org/news), parecido como foi feito no problema do rato e o labirinto.

### A oque chegamos:

Em resumo conseguimos montar o game utilizando o Pygames, e realizando uma cópia do que o nosso algorítimo gera como solução, porem a dificuldade está em ele jogar por nos imprimindo no Pygames.. Vamos visualizar!

Hoje nosso algorítimo ao rodar nos retorna o melhor caminho possível para solução da travessia, seguindo as regras definidas a ele.

#### OBS:
TravesiaComAlgoritimo.py é o algorítimo que realiza a travessia com algorítimo, entregado inicialmente.

TravesiaEmPyGames.py é o código que roda o jogo em Pygames.

TravesiaPyGames+Algoritimo.py é onde esta o projeto final da junção dos dois códigos.


### Resultado:

```sh
Execução da resulução do problema:
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
| FILHA_1    |                |            |
| FILHA_2    |                |            |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
| FILHA_1    |                |            |
| FILHA_2    |                |            |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
| FILHA_1    |                |            |
| FILHA_2    |                |            |
|            |                | LADRAO     |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
| FILHA_2    |                |            |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
| FILHA_2    |                |            |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
| PAI        |                |            |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
| PAI        |                |            |
| MAE        |                |            |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
| PAI        |                |            |
|            |                | MAE        |
| FILHO_1    |                |            |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
|            |                | FILHO_1    |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
|            |                | FILHO_1    |
| FILHO_2    |                |            |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
|            |                | FILHO_1    |
|            |                | FILHO_2    |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
|            |                | POLICIAL   |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
|            |                | FILHO_1    |
|            |                | FILHO_2    |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
| LADRAO     |                |            |
| POLICIAL   |                |            |
 
|            |                |            |
|            |                | PAI        |
|            |                | MAE        |
|            |                | FILHO_1    |
|            |                | FILHO_2    |
|            |                |            |
|            |                | FILHA_1    |
|            |                | FILHA_2    |
|            |                | LADRAO     |
|            |                | POLICIAL   |
```

E para obtermos o mesmo resultado no nosso jogo em Pygames, podemos fazer:

![20220713_192433](https://user-images.githubusercontent.com/52337680/178847607-f4268935-0108-4169-8582-6e579a7ed34c.gif)

### Vamos ver brevemente o código:

Vamos definir nosso Person que serias nossos objetos e as condições do barco:

![image](https://user-images.githubusercontent.com/52337680/178849717-547dc28d-ab38-446e-849f-f5de8b4f5bf6.png)

Definimos o Barco e suas movimentações pelo jogo:

![image](https://user-images.githubusercontent.com/52337680/178849809-774a12eb-2edc-4b43-a066-96f80f7e6c07.png)

Aqui definimos as regras e cada personagem de nossa travessia.

![image](https://user-images.githubusercontent.com/52337680/178849866-99aaf52e-dce4-48b4-a78c-dbe0cdc1eb98.png)

E por fim o While que percorre as condições e a regra que atualiza a tela:

![image](https://user-images.githubusercontent.com/52337680/178849980-a459bd5c-ece6-47a2-89eb-e945a53a1cfb.png)

### Bom..

Com um jogo em Pygames e um algorítimo que joga automaticamente, agora teríamos apenas que juntar os 2 códigos, muito simples não? bom se fosse...

Tenteamos de diversas maneiras juntar os 2 códigos e mesclar em um só, poremos ainda não obtemos o melhor resultado.

Por hora conseguimos ele identificar a lista de melhor resposta do algorítimo e tentar movimentar os itens, porem o resultado ainda não é o esperado.

Para isso tentamos fazer uma regra simples de filtrar a lista e obtermos apenas o melhor resultado, e com alguns if and else para validar as informações:

```py
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
```

Parece uma solução suja, mas no debug ele pega perfeitamente o que precisamos, porem ainda não chegamos no refinamento perfeito onde ele realiza o que queremos:

Ele nos retorna o melhor resultado de movimentação na lista e faz uso dela:

```py
[['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'D', 'D'], ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'E', 'E'], ['E', 'E', 'E', 'E', 'D', 'E', 'D', 'D', 'D'], ['E', 'E', 'E', 'E', 'D', 'E', 'E', 'E', 'E'], ['E', 'D', 'E', 'E', 'D', 'D', 'E', 'E', 'D'], ['E', 'E', 'E', 'E', 'D', 'D', 'E', 'E', 'E'], ['D', 'D', 'E', 'E', 'D', 'D', 'E', 'E', 'D'], ['E', 'D', 'E', 'E', 'D', 'D', 'E', 'E', 'E'], ['E', 'D', 'E', 'E', 'D', 'D', 'D', 'D', 'D'], ['E', 'E', 'E', 'E', 'D', 'D', 'D', 'D', 'E'], ['D', 'D', 'E', 'E', 'D', 'D', 'D', 'D', 'D'], ['E', 'D', 'E', 'E', 'D', 'D', 'D', 'D', 'E'], ['D', 'D', 'D', 'E', 'D', 'D', 'D', 'D', 'D'], ['D', 'D', 'D', 'E', 'D', 'D', 'E', 'E', 'E'], ['D', 'D', 'D', 'D', 'D', 'D', 'E', 'D', 'D'], ['D', 'D', 
'D', 'D', 'D', 'D', 'E', 'E', 'E'], ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']]
```

:/ 

![20220713_195528](https://user-images.githubusercontent.com/52337680/178850803-af23e748-00fc-46df-9437-4e52b7e51fce.gif)
