def is_palindrome(text):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Remove espaços, pontuação e converte para minúsculas.
    
    Parâmetros:
    text (str): Texto para verificar
    
    Retorna:
    bool: True se for palíndromo, False caso contrário
    """
    import re
    # Remove espaços, pontuação e converte para minúsculas
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    # Verifica se o texto é igual ao seu reverso
    return clean_text == clean_text[::-1]

def palindrome_checker():
    print("=== VERIFICADOR DE PALÍNDROMO ===")
    print("Um palíndromo é uma palavra ou frase que se lê igual de trás para frente")
    print("Exemplos: 'arara', 'A cara rajada da jararaca', 'anotaram a data da maratona'")
    
    while True:
        text = input("\nDigite uma palavra ou frase (ou 'sair' para encerrar): ")
        
        if text.lower() == 'sair':
            print("Verificador encerrado!")
            break
        
        if not text.strip():
            print("Erro: Digite algum texto!")
            continue
        
        result = is_palindrome(text)
        
        print(f"\nTexto analisado: '{text}'")
        
        if result:
            print("Resultado: Sim")
            print("✓ Este texto É um palíndromo!")
        else:
            print("Resultado: Não") 
            print("✗ Este texto NÃO é um palíndromo!")
        
        print("-" * 40)

if __name__ == "__main__":
    palindrome_checker()