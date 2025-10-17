import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Gera uma senha aleatória com os critérios especificados.
    
    Parâmetros:
    length (int): Comprimento da senha
    use_letters (bool): Incluir letras
    use_numbers (bool): Incluir números
    use_symbols (bool): Incluir símbolos
    
    Retorna:
    str: Senha gerada
    """
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "Erro: Nenhum tipo de caractere selecionado!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """
    Avalia a força da senha gerada.
    """
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Muito curta (mínimo 8 caracteres)")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Adicione letras minúsculas")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Adicione letras maiúsculas")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Adicione números")
        
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        feedback.append("Adicione símbolos especiais")
    
    if score <= 2:
        strength = "Fraca"
    elif score <= 4:
        strength = "Média"
    else:
        strength = "Forte"
    
    return strength, feedback

def password_generator():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    
    while True:
        try:
            print("\nConfiguração da senha:")
            length = int(input("Tamanho da senha (recomendado: 12-16): "))
            
            if length < 4:
                print("Erro: Tamanho mínimo é 4 caracteres!")
                continue
            if length > 128:
                print("Erro: Tamanho máximo é 128 caracteres!")
                continue
            
            print("\nTipos de caracteres (s/n):")
            use_letters = input("Incluir letras (a-z, A-Z)? [s]: ").lower()
            use_letters = use_letters != 'n'
            
            use_numbers = input("Incluir números (0-9)? [s]: ").lower()
            use_numbers = use_numbers != 'n'
            
            use_symbols = input("Incluir símbolos (!@#$...)? [s]: ").lower()
            use_symbols = use_symbols != 'n'
            
            if not any([use_letters, use_numbers, use_symbols]):
                print("Erro: Selecione pelo menos um tipo de caractere!")
                continue
            
            password = generate_password(length, use_letters, use_numbers, use_symbols)
            strength, feedback = password_strength(password)
            
            print("\n" + "="*50)
            print("SENHA GERADA")
            print("="*50)
            print(f"Senha: {password}")
            print(f"Comprimento: {len(password)} caracteres")
            print(f"Força: {strength}")
            
            if feedback:
                print("\nPara melhorar a segurança:")
                for tip in feedback:
                    print(f"• {tip}")
            
            print("\nComposição:")
            print(f"• Letras: {'✓' if use_letters else '✗'}")
            print(f"• Números: {'✓' if use_numbers else '✗'}")
            print(f"• Símbolos: {'✓' if use_symbols else '✗'}")
            print("="*50)
            
            another = input("\nGerar outra senha? (s/n): ")
            if another.lower() != 's':
                print("Gerador de senhas encerrado!")
                break
                
        except ValueError:
            print("Erro: Digite um número válido para o tamanho!")
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break

if __name__ == "__main__":
    password_generator()