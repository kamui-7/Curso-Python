"""
-> É uma lista de listas de numeros inteiros.
-> As listas internas tem o tamanho de 10 elementos.
-> As listas internas contem numeros entre 1 a 10 e eles podem ser duplicados

Exercicio

-> Crie uma função que encontra o primeiro numero duplicado, considerando-o o segundo
numero como a duplicação.
    Requisitos:
        A ordem dos numero duplicados é considerada a partir da segunda
        ocorrencia (o numero duplicado em si).
        Exemplo: [1,2,3,->3<-,2,1] --> 1 , 2 e 3 são duplicados, mas como temos que levar em consideração
        o segundo numero e quando ele se duplica então o numero é o 3.
        Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [3,4,6,7,3,3,1,2,3,5],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [7,7,8,10,4,10,3,4,2,3],
    [10,7,4,2,8,9,4,3,3,3],
    [8,3,4,9,2,4,4,8,8,1],
    [2,3,1,8,3,8,10,3,1,2],
    [9,3,3,7,6,1,2,8,3,10],
    [4,6,8,1,1,6,6,3,2,9],
]

