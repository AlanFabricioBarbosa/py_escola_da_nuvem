def analyze_numbers():
    even_numbers = []
    odd_numbers = []
    
    print("=== ANALISADOR DE NÚMEROS ===")
    print("Digite números para análise (digite 'fim' para encerrar)")
    
    while True:
        user_input = input("\nDigite um número (ou 'fim' para encerrar): ")
        
        if user_input.lower() == 'fim':
            break
        
        try:
            number = int(user_input)
            
            if number % 2 == 0:
                even_numbers.append(number)
                print(f"O número {number} é PAR")
            else:
                odd_numbers.append(number)
                print(f"O número {number} é ÍMPAR")
                
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos!")
    
    print("\n" + "="*40)
    print("RELATÓRIO DE ANÁLISE")
    print("="*40)
    
    total_numbers = len(even_numbers) + len(odd_numbers)
    
    if total_numbers > 0:
        print(f"Total de números analisados: {total_numbers}")
        print(f"Números pares: {len(even_numbers)}")
        print(f"Números ímpares: {len(odd_numbers)}")
        
        if even_numbers:
            print(f"\nLista de números pares: {even_numbers}")
            print(f"Soma dos pares: {sum(even_numbers)}")
        
        if odd_numbers:
            print(f"\nLista de números ímpares: {odd_numbers}")
            print(f"Soma dos ímpares: {sum(odd_numbers)}")
        
        percentage_even = (len(even_numbers) / total_numbers) * 100
        percentage_odd = (len(odd_numbers) / total_numbers) * 100
        
        print(f"\nEstatísticas:")
        print(f"Porcentagem de pares: {percentage_even:.1f}%")
        print(f"Porcentagem de ímpares: {percentage_odd:.1f}%")
        
    else:
        print("Nenhum número foi analisado!")

if __name__ == "__main__":
    analyze_numbers()