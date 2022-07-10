# Crie um programa que leia o salário de um vendedor e o valor total de vendas no mês. 
# Se o valor de vendas no mês do funcionário for maior que 5000,
# ele terá um aumento de 20% no valor final de seu salário.
# Ao final do programa exiba o salário final do usuário na tela


salario = float(input('Qual o valor do salário? '))
vendas = float(input('Qual o valor das vendas? '))
aumento = salario * 0.2

if vendas > 5000 :
    salario = (salario + aumento)
    print('Parabéns, você ganhou um aumento, seu novo salário é {}'.format(salario))

else:
    print('Suas vendas não bateram a meta, valor do salário permanece R${}'.format(salario))
