def contar_caracteres(string):
    # 5- TODO: Inicialize um dicionário vazio "contador" para armazenar as contagens de caracteres:
    # O dicionário 'contador' armazenará os caracteres como chaves e suas contagens como valores.
    contador = {}

    # 7- TODO: Itere através de cada caractere na string string:
    # O loop 'for' percorre cada caractere individualmente na string de entrada.
    for caractere in string:
        
        # 8- TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if caractere in contador:
            # Se o caractere JÁ existe como chave, incrementamos a sua contagem (o valor).
            contador[caractere] += 1
        else:
            # Se o caractere NÃO existe como chave, adicionamos ele ao dicionário 
            # e inicializamos sua contagem com 1.
            contador[caractere] = 1
            
    # Retornamos o dicionário final com as contagens.
    return contador

# 12- Solicita entrada do usuário
entrada = input("")

# 14- Chamamos a função e armazenamos o resultado
resultado = contar_caracteres(entrada)

# 15- Imprimimos o dicionário de resultado
print(resultado)