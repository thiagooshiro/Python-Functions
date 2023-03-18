amigos_aniversariantes = ['Bruna', 'Letícia']

todos_amigos = {
    "Amanda": { "aniversário": '22/02', "presente": 'Livros'},
    "Bruna": {"aniversário": '18/03', "presente": 'Artesanato'},
    "Pedro": {"aniversário": '20/09', "presente": 'Itens de esporte'},
    "Letícia": {"aniversário": '02/03', "presente": 'Plantinhas'},
}



def lista_amigos(lista, dictionary):
    for name in lista:
        if name in dictionary:
            print(f"{name}: {dictionary[name]['presente']}")

lista_amigos(amigos_aniversariantes, todos_amigos)

