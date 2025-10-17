import re

def check_password_security(password):
    criteria = {
        'length': len(password) >= 8,
        'has_number': bool(re.search(r'\d', password))
    }
    
    return criteria

def password_validator():
    print("=== VALIDADOR DE SENHA ===")
    print("Critérios de segurança:")
    print("• Pelo menos 8 caracteres")
    print("• Pelo menos um número")
    
    while True:
        password = input("\nDigite sua senha (ou 'sair' para encerrar): ")
        
        if password.lower() == 'sair':
            print("Validador encerrado!")
            break
        
        criteria = check_password_security(password)
        
        print(f"\n--- ANÁLISE DA SENHA ---")
        print(f"Senha: {'*' * len(password)}")
        print(f"Comprimento: {len(password)} caracteres")
        
        print("\nCritérios atendidos:")
        print(f"✓ Pelo menos 8 caracteres: {'SIM' if criteria['length'] else 'NÃO'}")
        print(f"✓ Contém pelo menos um número: {'SIM' if criteria['has_number'] else 'NÃO'}")
        
        all_criteria_met = all(criteria.values())
        
        if all_criteria_met:
            print("\n🟢 SENHA SEGURA! Todos os critérios foram atendidos.")
        else:
            print("\n🔴 SENHA INSEGURA! Alguns critérios não foram atendidos.")
            print("\nRecomendações:")
            if not criteria['length']:
                print("• Aumente o comprimento da senha para pelo menos 8 caracteres")
            if not criteria['has_number']:
                print("• Adicione pelo menos um número à senha")
        
        print("-" * 30)

if __name__ == "__main__":
    password_validator()