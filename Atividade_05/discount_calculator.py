def calculate_discount(original_price, discount_percentage):
    """
    Calcula o valor do desconto baseado em uma porcentagem.
    
    Parâmetros:
    original_price (float): Preço original do produto
    discount_percentage (float): Porcentagem de desconto
    
    Retorna:
    tuple: (discount_value, final_price)
    """
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    return round(discount_value, 2), round(final_price, 2)

def discount_calculator():
    print("=== CALCULADORA DE DESCONTO ===")
    
    while True:
        try:
            original_price = float(input("\nDigite o preço original do produto: R$ "))
            
            if original_price <= 0:
                print("Erro: O preço deve ser maior que zero!")
                continue
            
            discount_percentage = float(input("Digite a porcentagem de desconto (%): "))
            
            if discount_percentage < 0 or discount_percentage > 100:
                print("Erro: A porcentagem deve estar entre 0 e 100!")
                continue
            
            discount_value, final_price = calculate_discount(original_price, discount_percentage)
            savings_percentage = (discount_value / original_price) * 100
            
            print("\n" + "="*40)
            print("CÁLCULO DE DESCONTO")
            print("="*40)
            print(f"Preço original: R$ {original_price:.2f}")
            print(f"Desconto ({discount_percentage}%): R$ {discount_value:.2f}")
            print(f"Preço final: R$ {final_price:.2f}")
            print(f"Você economiza: R$ {discount_value:.2f}")
            print("="*40)
            
            another = input("\nDeseja calcular outro desconto? (s/n): ")
            if another.lower() != 's':
                print("Obrigado por usar a calculadora de desconto!")
                break
                
        except ValueError:
            print("Erro: Digite apenas números válidos!")

if __name__ == "__main__":
    discount_calculator()