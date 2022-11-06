n = s = 0
while n != 999:  # -> Jeito errado, pois soma o flag também (999) #
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}.'.format(s))
print('FIM')
