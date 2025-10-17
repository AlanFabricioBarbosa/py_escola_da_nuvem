import requests
import json

def fetch_random_user():
    """
    Busca um usuário fictício aleatório da API.
    
    Retorna:
    dict: Dados do usuário ou None se houver erro
    """
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        user = data['results'][0]
        
        return {
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'country': user['location']['country'],
            'city': user['location']['city'],
            'phone': user['phone'],
            'gender': user['gender'],
            'age': user['dob']['age'],
            'picture': user['picture']['large']
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
    except KeyError as e:
        print(f"Erro ao processar dados da API: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def display_user(user_data):
    """
    Exibe as informações do usuário de forma formatada.
    """
    print("\n" + "="*40)
    print("USUÁRIO FICTÍCIO GERADO")
    print("="*40)
    print(f"Nome: {user_data['name']}")
    print(f"E-mail: {user_data['email']}")
    print(f"País: {user_data['country']}")
    print(f"Cidade: {user_data['city']}")
    print(f"Telefone: {user_data['phone']}")
    print(f"Gênero: {user_data['gender'].title()}")
    print(f"Idade: {user_data['age']} anos")
    print("="*40)

def random_user_generator():
    print("=== GERADOR DE USUÁRIO FICTÍCIO ===")
    print("Buscando usuários aleatórios da API RandomUser...")
    
    while True:
        print("\nPressione Enter para gerar um usuário ou digite 'sair' para encerrar")
        user_input = input("Comando: ")
        
        if user_input.lower() == 'sair':
            print("Gerador encerrado!")
            break
        
        print("Buscando usuário... Aguarde...")
        user_data = fetch_random_user()
        
        if user_data:
            display_user(user_data)
        else:
            print("\n❌ Falha ao buscar usuário!")
            print("Possíveis causas:")
            print("• Problema de conexão com a internet")
            print("• API temporariamente indisponível")
            print("• Servidor sobrecarregado")
            print("\nTente novamente em alguns instantes.")

if __name__ == "__main__":
    random_user_generator()