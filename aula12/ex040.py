n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
