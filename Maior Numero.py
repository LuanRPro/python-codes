#Faça um programa que leia dois números e exiba o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2 :
    print('o número {} é maior'.format(n1))

elif n1 == n2 :
    print('Os dois números são iguais.')

else :
    print('o número {} é maior'.format(n2))
