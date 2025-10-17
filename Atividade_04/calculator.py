def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida"

def calculator():
    print("=== CALCULADORA ===")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    while True:
        try:
            choice = input("\nEscolha uma operação (1-4) ou 'q' para sair: ")
            
            if choice.lower() == 'q':
                print("Calculadora encerrada!")
                break
            
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = "/"
                
                print(f"\nResultado: {num1} {operation} {num2} = {result}")
            else:
                print("Opção inválida! Escolha uma operação válida.")
                
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    calculator()