
# somar = 2 + 3

# subtrair = 5 - 4

# multiplicar = 4 * 3

# dividir = 4 // 2

aniversariantes_do_mes = ['Bruna', 'Letícia']

todos_amigos = {
    "Amanda": { "aniversário": '22/02', "presente": 'Livros'},
    "Bruna": {"aniversário": '18/03', "presente": 'Artesanato'},
    "Pedro": {"aniversário": '20/09', "presente": 'Itens de esporte'},
    "Letícia": {"aniversário": '02/03', "presente": 'Plantinhas'},
}

# a função deve imprimir nome da pessoa aniversariante: presente favorito;

def lista_amigos():
    pass



def somar(numA, numB):
    resultado = numA + numB
    return resultado


def subtrair(A, B):
    sub = A - B
    return sub

def multiplicar(A, B):
    mult = A * B
    return mult

def dividir(A, B):
    div = A // B
    return div


def menu():
    print('Bem vindos à Calculadora!')
    print('1. adição')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')

    escolha = int(input('Escolha sua operação (1, 2, 3, 4) '))
    if not 1 <= escolha <= 4 :
        print('Operação inválida')
    else:
        return escolha

continua = True


while continua:
    
    escolha = menu()
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))

    if escolha == 1:
        print(somar(num_1, num_2))
    elif escolha == 2:
        print(subtrair(num_1, num_2))
    elif escolha == 3:
        print(multiplicar(num_1, num_2))
    elif escolha == 4:
        print(dividir(num_1, num_2))
    else:
        print('Escolha uma operação através dos números')
    
    controle = int(input('Você deseja fazer outra conta? Sim(1), Não(2) '))
    if controle == 2:
        continua = False
    elif controle == 1:
        continua = True
    else:
        print('Escolha inválida')
        break