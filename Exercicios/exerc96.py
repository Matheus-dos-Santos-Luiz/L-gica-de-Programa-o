def controle():
    print("Controle de Terrenos")
    print('-' *30)
controle()

larg = float(input("Largura (m): "))
compr = float(input("Comprimento (m): ")) 

def calc(larg, compr):
    area = larg * compr
    print(f'A área de um terreno {larg}x{compr} é de {area}m²')

    
calc(larg, compr)