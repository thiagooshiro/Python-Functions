def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multy(a, b):
    return a * b


def division(a, b):
    return a / b


print('Bem vindo à calculadora! Escolha a operação: ')
print('a.adição')
print('b.subtração')
print('c.multiplicação')
print('d.divisão')

choice = input('Escolha uma operação (a, b, c, d): ')

num_1 = int(input('Digite o primeiro valor: '))
num_2 = int(input('Digite o segundo número: '))

if choice is 'a':
    print(num_1, '+', num_2, '=', add(num_1, num_2))
elif choice is 'b':
    print(num_1, '-', num_2, '=', sub(num_1, num_2))
elif choice is 'c':
    print(num_1, '*', num_2, '=', multy(num_1, num_2))
elif choice is 'd':
    print(num_1, '/', num_2, '=', division(num_1, num_2))
else:
    print('Operação inválida')
