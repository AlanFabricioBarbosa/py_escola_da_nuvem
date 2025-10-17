import requests
import re

def validate_cep(cep):
    """
    Valida o formato do CEP brasileiro.
    
    Parâmetros:
    cep (str): CEP a ser validado
    
    Retorna:
    str: CEP formatado ou None se inválido
    """
    # Remove caracteres não numéricos
    clean_cep = re.sub(r'\D', '', cep)
    
    # Verifica se tem 8 dígitos
    if len(clean_cep) != 8:
        return None
    
    return clean_cep

def fetch_cep_info(cep):
    """
    Consulta informações de um CEP na API ViaCEP.
    
    Parâmetros:
    cep (str): CEP a ser consultado
    
    Retorna:
    dict: Informações do CEP ou None se houver erro
    """
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Verifica se o CEP foi encontrado
        if 'erro' in data:
            return None
        
        return {
            'cep': data.get('cep', ''),
            'logradouro': data.get('logradouro', 'Não informado'),
            'bairro': data.get('bairro', 'Não informado'),
            'cidade': data.get('localidade', 'Não informado'),
            'estado': data.get('uf', 'Não informado'),
            'complemento': data.get('complemento', ''),
            'ibge': data.get('ibge', ''),
            'gia': data.get('gia', ''),
            'ddd': data.get('ddd', '')
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
    except ValueError as e:
        print(f"Erro ao processar resposta da API: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def display_cep_info(cep_data):
    """
    Exibe as informações do CEP de forma formatada.
    """
    print("\n" + "="*40)
    print("INFORMAÇÕES DO CEP")
    print("="*40)
    print(f"CEP: {cep_data['cep']}")
    print(f"Logradouro: {cep_data['logradouro']}")
    print(f"Bairro: {cep_data['bairro']}")
    print(f"Cidade: {cep_data['cidade']}")
    print(f"Estado: {cep_data['estado']}")
    
    if cep_data['complemento']:
        print(f"Complemento: {cep_data['complemento']}")
    if cep_data['ddd']:
        print(f"DDD: {cep_data['ddd']}")
    
    print("="*40)

def cep_lookup():
    print("=== CONSULTA DE CEP ===")
    print("Digite um CEP para consultar suas informações")
    print("Formato aceito: 12345-678 ou 12345678")
    
    while True:
        cep_input = input("\nDigite um CEP (ou 'sair' para encerrar): ")
        
        if cep_input.lower() == 'sair':
            print("Consulta encerrada!")
            break
        
        # Valida o CEP
        clean_cep = validate_cep(cep_input)
        
        if not clean_cep:
            print("❌ CEP inválido! Use o formato: 12345-678 ou 12345678")
            continue
        
        print(f"Consultando CEP {clean_cep}... Aguarde...")
        cep_data = fetch_cep_info(clean_cep)
        
        if cep_data:
            display_cep_info(cep_data)
        else:
            print("\n❌ Falha na consulta!")
            print("Possíveis causas:")
            print("• CEP não encontrado")
            print("• Problema de conexão com a internet")
            print("• API temporariamente indisponível")
            print("\nVerifique o CEP e tente novamente.")

if __name__ == "__main__":
    cep_lookup()