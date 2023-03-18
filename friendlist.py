amigos_aniversariantes = ['Bruna', 'Letícia']

todos_amigos = {
    "Amanda": { "aniversário": '22/02', "presente": 'Livros'},
    "Bruna": {"aniversário": '18/03', "presente": 'Artesanato'},
    "Pedro": {"aniversário": '20/09', "presente": 'Itens de esporte'},
    "Letícia": {"aniversário": '02/03', "presente": 'Plantinhas'},
}



def lista_amigos(lista, dictionary):
    
    # Desafio é imprimir:
# nome dos aniversariantes seguido do presente favorito;

aniversariantes_do_mes = ['Bruna', 'Letícia']

todos_amigos = {
    "Amanda": { "aniversário": '22/02', "presente": 'Livros'},
    "Bruna": {"aniversário": '18/03', "presente": 'Artesanato'},
    "Pedro": {"aniversário": '20/09', "presente": 'Itens de esporte'},
    "Letícia": {"aniversário": '02/03', "presente": 'Plantinhas'},
}

#Sem parmetros
'''def amigos():
    for item in todos_amigos:
        for nome in aniversariantes_do_mes:
            if item == nome:
                print(nome, todos_amigos[item]["aniversário"], todos_amigos[item]["presente"])

amigos()'''

#conforme o exercicio
def lista_amigos(lista, dicionario):
    for nome in lista:
        for item in dicionario:
            if nome == item:
                print(nome, dicionario[item]["aniversário"], dicionario[item]["presente"])

lista_amigos(aniversariantes_do_mes, todos_amigos)

lista_amigos(amigos_aniversariantes, todos_amigos)

