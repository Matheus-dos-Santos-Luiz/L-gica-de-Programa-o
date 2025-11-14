try:
    arquivo = open('meuarquivo.py')
except FileNotFoundError:
    print("Arquivo nao encontrado!")
