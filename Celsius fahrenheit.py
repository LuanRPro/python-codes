# Conversor de temperaturas de Fahrenheit para Celsius e de Celsius para Fahrenheit

valor = 0
celsius = 0
fahrenheit = 0

escolha = input('Informe se deseja converter uma temperatura\nde Celsius para Fahrenheit(F) ou Fahrenheit para Celsius(C)\nutilizando (C) ou (F): ')

# Valida se a pessoa escolheu uma das opções corretamente
while escolha != 'C' and escolha != 'F':

    print('\nEntrada inválida, utilize apenas C ou F (maiúsculos)\n\n')
    print('Tente de Novo:\n\n')
    escolha = input('Informe se deseja converter uma temperatura de Celsius para Fahrenheit(F) ou\nFahrenheit para Celsius(C)utilizando (C) ou (F): ')

# Uma vez que a opção foi escolhida corretamente, continua para o cálculo
else :

    valor = float(input('\nAgora informe a temperatura: '))
    celsius = (valor - 32) / 1.8
    fahrenheit = valor * 1.8 + 32

# Fahrenheit para Celsius
    if escolha == 'C' :
        print('\n{}° fahrenheit é igual a {:.2f}° graus celsius'.format(valor, celsius))

# Celsius para Fahrenheit
    else:
        print('\n{}° graus celsius é igual a {:.2f}° fahrenheit'.format(valor, fahrenheit))
