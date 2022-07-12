# CONVERSOR DE MEDIDAS DE TEMPERATURA

# Declaração de variáveis

valor = 0
medidas = ['K', 'F', 'C']
kelvinFahrenheit = 0
kelvinCelcius = 0
fahrenheitCelsius = 0
fahrenheitKelvin = 0
celsiusFahrenheit = 0
celsiusKelvin = 0

# Primeira entrada do usuário
escolha1 = input('Informe a medida de temperatura que será transformada utilizando\n(K) para Kelvin, (F) para Fahrenheit e (C) para Celsius: ')

# Valida se a pessoa escolheu a primeira medida corretamente
while escolha1 not in medidas :

    print('\nEntrada inválida, utilize apenas K, F ou C (maiúsculos)\n\n')
    print('Tente de Novo:\n\n')
    escolha1 = input('Informe a medida de temperatura que será transformada utilizando\n(K) para Kelvin, (F) para Fahrenheit e (C) para Celsius: ')

# Uma vez que a primeira medida foi escolhida corretamente, continua para informar para qual medida deve ser transformada
else :
# Segunda entrada do usuário
    escolha2 = input('\nAgora informe para qual medida de temperatura deseja converter utilizando\n(K) para Kelvin, (F) para Fahrenheit e (C) para Celsius: ')
# Valida se a pessoa escolheu a segunda medida corretamente
    while escolha2 not in medidas :

        print('\nEntrada inválida, utilize apenas K, F ou C (maiúsculos)\n\n')
        print('Tente de Novo:\n\n')
        escolha2 = input('Agora informe para qual medida de temperatura deseja converter utilizando\n(K) para Kelvin, (F) para Fahrenheit e (C) para Celsius: ')

    else :
# Recebimento do valor a ser calculado e fórmulas
# Verifica se o valor da entrada é válido
        while True:
            try :
                valor = float(input('\nAgora informe o valor da temperatura: '))
            except ValueError :
                print('\nApenas números são aceitos! Tente de novo:\n')
                continue
            else :
                break

        kelvinFahrenheit = 1.8 * (valor - 273) + 32
        kelvinCelcius = valor - 273.15
        fahrenheitCelsius = (valor - 32) / 1.8
        fahrenheitKelvin = (valor - 32) * (5/9) + 273.15
        celsiusFahrenheit = valor * 1.8 + 32
        celsiusKelvin = valor + 273.15

# Kelvin para Fahrenheit
        if escolha1 == 'K' and escolha2 == 'F' :
            print('\n{}° Kelvin é igual a {:.3f}° Fahrenheit'.format(valor, kelvinFahrenheit))

# Kelvin para Celsius
        elif escolha1 == 'K' and escolha2 == 'C' :
            print('\n{}° Kelvin é igual a {:.3f}° graus celsius'.format(valor, kelvinCelcius))

# Fahrenheit para Celsius
        elif escolha1 == 'F' and escolha2 == 'C' :
            print('\n{}° Fahrenheit é igual a {:.3f}° graus Celsius'.format(valor, fahrenheitCelsius))

# Fahrenheit para Kelvin
        elif escolha1 == 'F' and escolha2 == 'K' :
            print('\n{}° Fahrenheit é igual a {:.3f}° Kelvin'.format(valor, fahrenheitKelvin))

# Celsius para Fahrenheit
        elif escolha1 == 'C' and escolha2 == 'F' :
            print('\n{}° graus Celsius é igual a {:.3f}° Fahrenheit'.format(valor, celsiusFahrenheit))

# Celsius para Kelvin
        elif escolha1 == 'C' and escolha2 == 'K' :
            print('\n{}° graus Celsius é igual a {:.3f}° Kelvin'.format(valor, celsiusKelvin))
