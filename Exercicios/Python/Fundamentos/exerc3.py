def conta_vogais(texto):
    # 1. TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    # Definimos um conjunto (set) de vogais sem acentuação, incluindo maiúsculas e minúsculas.
    # Usamos um conjunto para pesquisa rápida (tempo constante O(1)).
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # 2. TODO: Inicialize um contador para contar as vogais:
    contador = 0
    
    # 3. Iteramos pelos caracteres da string
    for char in texto:
        # 4. TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
            contador += 1
            
    # 5. Retorna o contador: Após percorrer todos os caracteres da string, 
    # retorna o valor do contador, que representa o número total de vogais na string.
    return contador

# 6. Solicitamos ao usuário que insira uma string
texto = input()

# 7. Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")