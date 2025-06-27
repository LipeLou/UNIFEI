'''
Nos últimos dias, o papo das diferenças entre gerações ficou mais proeminente nas redes sociais. E
isso aconteceu por uma diferença importante: os millennials oficialmente já escalonaram, na visão
da Geração Z, para uma idade na qual já não são mais considerados jovens. Hoje, são vistos pelos
adolescentes e jovens adultos como pessoas mais velhas que tem certos costumes que já estão fora de
moda ou, como a Geração Z gosta de falar, os millennials são cringe.
Os millennials tem o costume de achar que os mais novos, da Geração Z, deveriam ser mais novos do
que realmente são. Por exemplo, um millennial não aceita que uma pessoa que nasceu em 2015 possa
ter 10 anos: quem tem 10 anos deveria ter nascido em 2005!
Um millennial sente o tempo passar na metade do tempo: se uma pessoa da Geração Z nasceu 𝑥 anos
atrás, um millennial acredita que ela deveria ter nascido 2𝑥 anos atrás para ter a idade que ela tem.
Assumindo que o ano é 2025, escreva um programa que, dado o ano 𝑌 que uma pessoa da Geração Z
nasceu, calcule o ano que um millennial acredita que ela deveria ter nascido.

Entrada
A entrada consiste em apenas um número 𝑌 (2010 ≤ 𝑌 ≤ 2020), o ano em que a pessoa da Geração Z
nasceu.

Saída
Imprima um único número: o ano que um millennial acredita que a pessoa da Geração Z deveria ter
nascido para ter a idade que ela tem, dado que estamos no ano 2025.

Exemplos

Entrada  |  Saída
2015        2005

Entrada  |  Saída
2018        2011

'''

def ano_gen_z(ano):
    idade_gen_z = 2025 - ano
    idade_min = idade_gen_z * 2
    ano_gen_z = 2025 - idade_min

    return ano_gen_z

print(ano_gen_z(2015))
print(ano_gen_z(2018))