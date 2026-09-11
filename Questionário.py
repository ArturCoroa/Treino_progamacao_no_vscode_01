# Questionário que aprendi hoje - com bloqueio de idade

NOME = input('Qual seu nome? ')
IDADE = int(input('Qual sua idade? '))
ALTURA = input('Qual sua altura? ')
COR = input('Qual sua cor favorita? ')
ANIMAL = input('Qual seu animal favorito? ')
HOBBIE = input('Qual seu hobbie favorito? ')
TRABALHO = input('Qual seu trabalho? ')

if IDADE >= 18:
    print('\n--- DADOS COLETADOS ---')
    print(f'nome: {NOME}')
    print(f'idade: {IDADE}')
    print(f'altura: {ALTURA}')
    print(f'cor favorita: {COR}')
    print(f'animal favorito: {ANIMAL}')
    print(f'hobbie favorito: {HOBBIE}')
    print(f'trabalho: {TRABALHO}')
else:
    print('\nacesso negado!')
