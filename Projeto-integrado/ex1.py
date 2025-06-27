'''
Og, o ogro, possui vários filhos. E seus filhos, por sua vez, possuem vários filhos. Og quer saber quantos
netos ele tem. Mas ogros são péssimos em matemática. Portanto, Og quer sua ajuda: dado o número
de filhos que cada filho de Og tem, determine o número total de netos de Og.

Entrada
A entrada é descrita em duas linhas. A primeira linha contém um inteiro 𝑁 (1 ≤ 𝑁 ≤ 1000), indicando
o número de filhos de Og. A segunda linha possui 𝑁 inteiros 𝐹1, 𝐹2, . . . , 𝐹𝑁 . O número 𝐹𝑖 (0 ≤ 𝐹𝑖 ≤
1000, para todo 𝑖 entre 1 e 𝑁 inclusive) representa o número de filhos que o 𝑖-ésimo filho de Og possui.

Saída
Imprima uma linha contendo um único inteiro: o número de netos de Og.
Exemplos

Entrada    |    Saída
3                21
7 5 9

Entrada    |    Saída
2
40 98            138

'''

def og_netos():
    n_filhos = int(input())
    netos = 0
    for _ in range(0,n_filhos):
        filhos_do_filho = int(input())
        netos += filhos_do_filho

    return netos

print(og_netos())
