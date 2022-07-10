#Escreva um programa que informado o ano de nascimento e o ano atual, retorne a idade da pessoa.

anoAtual = int(input('Digite o ano atual:'))
anoDeNascimento = int(input('Digite o ano em que você nasceu:'))
idade = anoAtual - anoDeNascimento
print('Você tem', idade, 'anos, correto?')
