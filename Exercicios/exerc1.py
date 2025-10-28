nota1 = float(input("Digite a primeira nota (0/10): "))
nota2 = float(input("Digite a segunda nota (0/10): "))
nota3 = float(input("Digite a terceira nota (0/10): "))

if (0 <= nota1 <= 10) and (0 <= nota2 <= 10) and (0 <= nota3 <= 10):
    
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7:
        
        print(f'ALUNO PASSOU! Sua média foi {media:.2f}.')
    else:
        print(f'ALUNO REPROVOU. Sua média foi {media:.2f}.')

else:
    print('Parâmetro inválido! Pelo menos uma nota digitada está fora do intervalo [0/10].')