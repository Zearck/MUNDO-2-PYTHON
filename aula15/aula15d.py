n = s = 0
while True:  # -> Como é 'True' o programa continuará funcionando sem nenhum != para interrompe-lo #
    # -> Será pedido o input diversas vezes pelo progama (infinitamente) #
    n = int(input('Digite um número: '))
    if n == 999:  # -> Mas o if (se) por igual a 999 no número digitado, ele deverá parar, sendo assim pela função 'Break' #
        break
    s += n
print('A soma vale {}.'.format(s))
print('FIM')
