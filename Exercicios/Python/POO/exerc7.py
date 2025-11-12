# 1- TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    """
    """
    
    # 4- Define o método 'soma' que recebe dois números e retorna a soma.
    def soma(self, num1, num2):
        """
        Realiza a operação de soma entre dois números inteiros.
        
        Args:
            num1 (int): O primeiro número a ser somado.
            num2 (int): O segundo número a ser somado.
            
        Returns:
            int: O resultado da soma.
        """
        # A lógica da soma (adição) é encapsulada aqui.
        return num1 + num2

# --- Bloco de Execução Principal ---

# 5- Solicitando a entrada do usuário
# É importante ler a entrada fora da classe, no escopo principal.
try:
    print("")
    # Lendo e convertendo o primeiro número para inteiro
    num1 = int(input("")) 
    # Lendo e convertendo o segundo número para inteiro
    num2 = int(input(""))
    
    # 8- Criando uma instância (objeto) da Calculadora
    calc = Calculadora()
    
    # 11- Chamando o método 'soma' da instância 'calc' e passando as entradas do usuário
    resultado = calc.soma(num1, num2)
    
    # 12- Imprimindo o resultado
    print(f"{resultado}")

except ValueError:
    print("\nErro: Entrada inválida. Por favor, insira apenas números inteiros.")# 1- TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    """
    """
    
    # 4- Define o método 'soma' que recebe dois números e retorna a soma.
    def soma(self, num1, num2):
        """
        Realiza a operação de soma entre dois números inteiros.
        
        Args:
            num1 (int): O primeiro número a ser somado.
            num2 (int): O segundo número a ser somado.
            
        Returns:
            int: O resultado da soma.
        """
        # A lógica da soma (adição) é encapsulada aqui.
        return num1 + num2

# --- Bloco de Execução Principal ---

# 5- Solicitando a entrada do usuário
# É importante ler a entrada fora da classe, no escopo principal.
try:
    print("")
    # Lendo e convertendo o primeiro número para inteiro
    num1 = int(input("")) 
    # Lendo e convertendo o segundo número para inteiro
    num2 = int(input(""))
    
    # 8- Criando uma instância (objeto) da Calculadora
    calc = Calculadora()
    
    # 11- Chamando o método 'soma' da instância 'calc' e passando as entradas do usuário
    resultado = calc.soma(num1, num2)
    
    # 12- Imprimindo o resultado
    print(f"{resultado}")

except ValueError:
    print("\nErro: Entrada inválida. Por favor, insira apenas números inteiros.")