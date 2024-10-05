def soma_lista(lista):
    # Caso base: lista vazia retorna 0
    if len(lista) == 0:
        return 0
    # Caso recursivo: soma o primeiro elemento com o resto da lista
    else:
        return lista[0] + soma_lista(lista[1:])

# Testando a função
lista_numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(lista_numeros)
print(f"A soma da lista {lista_numeros} é: {resultado}")
