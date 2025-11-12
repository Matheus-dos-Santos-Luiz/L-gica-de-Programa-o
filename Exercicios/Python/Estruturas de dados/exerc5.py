def elementos_comuns(lista1_str, lista2_str):
    """
    Recebe duas strings de números separados por espaço,
    converte-as em conjuntos de inteiros, encontra a intersecção
    e retorna o resultado como uma lista.
    """
    
    # Bloco try/except para capturar ValueError caso a entrada não seja numérica.
    try:
        # Converte a primeira string de entrada (lista1_str) para um conjunto de inteiros
        # .split() divide a string por espaços; map(int, ...) converte cada item para inteiro.
        set1 = set(map(int, lista1_str.split()))
        
        # Converte a segunda string de entrada (lista2_str) para um conjunto de inteiros
        set2 = set(map(int, lista2_str.split()))
        
        # Encontra a intersecção dos dois conjuntos (elementos comuns)
        intersecao = set1.intersection(set2)
        
        # Retorna o resultado da intersecção como uma lista ordenada.
        # Usar list(sorted(...)) garante a lista e a ordem esperada para exibição.
        return list(sorted(intersecao))
        
    except ValueError:
        # Retorna a mensagem de erro se a conversão para int falhar (ex: entrada com letras)
        return "Entrada inválida."

if __name__ == "__main__":
    
    # 23- TODO: Solicita a primeira lista de números como string
    # Nota: O input() sem argumento de prompt (input()) é usado para corresponder à plataforma.
    lista1 = input()
    
    # 25- TODO: Solicita a segunda lista de números como string
    lista2 = input()
    
    # Chama a função elementos_comuns com as strings de entrada
    comuns = elementos_comuns(lista1, lista2)

    # Verifica o tipo de retorno para formatar a saída corretamente
    if comuns == "Entrada inválida.":
        print(comuns)
    else:
        # Exibe a lista dos elementos comuns, no formato 'Elementos comuns das duas listas: [3, 4]'
        print(f"Elementos comuns às duas listas: {comuns}")