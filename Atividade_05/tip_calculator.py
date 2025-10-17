def calculate_tip(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def tip_calculator():
    print("=== CALCULADORA DE GORJETA ===")
    
    while True:
        try:
            valor_conta = float(input("\nDigite o valor total da conta: R$ "))
            
            if valor_conta <= 0:
                print("Erro: O valor da conta deve ser maior que zero!")
                continue
            
            porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))
            
            if porcentagem_gorjeta < 0:
                print("Erro: A porcentagem não pode ser negativa!")
                continue
            
            gorjeta = calculate_tip(valor_conta, porcentagem_gorjeta)
            total_a_pagar = valor_conta + gorjeta
            
            print("\n" + "="*35)
            print("RESUMO DA CONTA")
            print("="*35)
            print(f"Valor da conta: R$ {valor_conta:.2f}")
            print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {gorjeta:.2f}")
            print(f"Total a pagar: R$ {total_a_pagar:.2f}")
            print("="*35)
            
            another = input("\nDeseja calcular outra gorjeta? (s/n): ")
            if another.lower() != 's':
                print("Obrigado por usar a calculadora de gorjeta!")
                break
                
        except ValueError:
            print("Erro: Digite apenas números válidos!")

if __name__ == "__main__":
    tip_calculator()