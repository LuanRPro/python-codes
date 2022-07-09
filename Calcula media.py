# Faça um programa que leia 4 notas e calcule a média.
# E se a média for maior ou igual a 6, escrever “Você foi Aprovado!” senão, escrever “Você foi Reprovado!”

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('Sua média foi {}'.format(media))

if media >= 6 :
    print('Você foi Aprovado!')

else :
    print('Você foi Reprovado!')