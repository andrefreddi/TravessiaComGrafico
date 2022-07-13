# Travessia Com Grafico
Desenvolvido por Andre Freddi e Willian Choaste

### Ideia:

A ideia inicial era juntar nosso algoritimo que realizava a o problema da travessia utilizando de um algoritimo para realizar a mesma e demonstrar de uma maneira bonita e dinamica para o usuario. utilizando da biblioteca [PyGames](https://www.pygame.org/news), Parecido como foi feito no problema do rato e o labirinto.

### O que chegamos:

Em resumo conseguimos montar o game utilizando o Pygames, e realizando uma copia do que o nosso algoritimo gera como solucao, porem a dificuldade esta em ele jogar por nos imprimindo no Pygames.. Vamos visualizar!

Hoje nosso algoritimo ao rodar nos retorna o melhor caminho possivel para solucao da travessia, seguindo as regras definidas a ele.

### Resultado:

OBS:
TravesiaComAlgoritimo.py é o algoritimo que realiza a travessia com algoritimo, entregado inicialmente.
TravesiaEmPyGames.py é o codigo que roda o jogo em Pygames.
TravesiaPyGames+Algoritimo.py é onde esta o projeto final da juncao dos dois codigos.

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


