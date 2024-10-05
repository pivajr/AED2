def potencia(base, expoente):
    # Caso base: qualquer número elevado a 0 é 1
    if expoente == 0:
        return 1
    # Caso recursivo: base * potencia(base, expoente - 1)
    else:
        return base * potencia(base, expoente - 1)

# Testando a função
base = 3
expoente = 4
resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é: {resultado}")
