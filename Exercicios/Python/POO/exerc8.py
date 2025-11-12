 class Pessoa:
    # O método __init__ é o construtor da classe, inicializando os atributos nome e idade.
    def __init__(self, nome, idade):
        self.nome = nome  # Atribui o nome passado como argumento ao atributo da instância
        self.idade = idade # Atribui a idade passada como argumento ao atributo da instância
    
    # 6- TODO: Crie um método para retornar as informações formatadas com Nome e Idade:
    def obter_info(self):
        """
        Retorna uma string formatada contendo o nome e a idade da pessoa.
        """
        # 12- Utiliza uma f-string para criar a representação formatada solicitada:
        # Nome: [nome] | Idade: [idade]
        return f"Nome: {self.nome},  Idade: {self.idade}"

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    
    # 18- 9: Entrada do usuário (Ajustado para o formato de teste)
    # Solicita o nome (string)
    # input() lê a primeira linha da entrada (o nome)
    nome = input()
    
    # 23- Solicita a idade e tenta converter para inteiro (int())
    # input() lê a segunda linha da entrada (a idade)
    try:
        idade = int(input())
    except ValueError:
        # Se a conversão falhar, trata o erro (embora o 'exit' não seja visível na saída padrão de teste)
        # Mantendo o tratamento de erro por boa prática, mas focando na lógica principal.
        # print("Erro: A idade deve ser um número inteiro.") 
        exit(1) # Encerra o programa se a idade for inválida

    # 31- TODO: Crie uma instância da pessoa:
    # Cria um objeto 'p' da classe Pessoa, passando as variáveis obtidas do usuário.
    p = Pessoa(nome, idade)
    
    # 35- TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
    # Chama o método obter_info() do objeto e imprime o resultado no console.
    resultado = p.obter_info()
    print(resultado)