import requests
from datetime import datetime

def fetch_currency_info(currency_code):
    """
    Consulta informações de uma moeda em relação ao Real (BRL).
    
    Parâmetros:
    currency_code (str): Código da moeda (ex: USD, EUR, GBP)
    
    Retorna:
    dict: Informações da moeda ou None se houver erro
    """
    try:
        # Formato da API: BRL para a moeda desejada
        url = f"https://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # A chave no JSON é invertida (ex: BRLAUD para AUD-BRL)
        key = f"BRL{currency_code}"
        
        if key not in data:
            return None
        
        currency_data = data[key]
        
        return {
            'code': currency_data.get('code', currency_code),
            'name': currency_data.get('name', 'Nome não disponível'),
            'current_value': float(currency_data.get('bid', 0)),
            'max_value': float(currency_data.get('high', 0)),
            'min_value': float(currency_data.get('low', 0)),
            'timestamp': int(currency_data.get('timestamp', 0)),
            'variation': float(currency_data.get('varBid', 0)),
            'percentage_change': float(currency_data.get('pctChange', 0))
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
    except KeyError as e:
        print(f"Moeda não encontrada: {e}")
        return None
    except ValueError as e:
        print(f"Erro ao processar dados: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def display_currency_info(currency_data):
    """
    Exibe as informações da moeda de forma formatada.
    """
    # Converte timestamp para data/hora legível
    update_time = datetime.fromtimestamp(currency_data['timestamp'])
    formatted_time = update_time.strftime("%d/%m/%Y %H:%M:%S")
    
    print("\n" + "="*50)
    print("COTAÇÃO DA MOEDA")
    print("="*50)
    print(f"Moeda: {currency_data['name']} ({currency_data['code']})")
    print(f"Valor atual: R$ {currency_data['current_value']:.4f}")
    print(f"Máxima do dia: R$ {currency_data['max_value']:.4f}")
    print(f"Mínima do dia: R$ {currency_data['min_value']:.4f}")
    print(f"Variação: R$ {currency_data['variation']:.4f}")
    print(f"Variação (%): {currency_data['percentage_change']:.2f}%")
    print(f"Última atualização: {formatted_time}")
    print("="*50)
    
    # Análise da tendência
    if currency_data['percentage_change'] > 0:
        trend = "📈 Alta (valorização)"
    elif currency_data['percentage_change'] < 0:
        trend = "📉 Baixa (desvalorização)"
    else:
        trend = "➡️ Estável"
    
    print(f"Tendência: {trend}")

def get_popular_currencies():
    """Retorna uma lista de moedas populares"""
    return {
        'USD': 'Dólar Americano',
        'EUR': 'Euro',
        'GBP': 'Libra Esterlina',
        'JPY': 'Iene Japonês',
        'CAD': 'Dólar Canadense',
        'AUD': 'Dólar Australiano',
        'CHF': 'Franco Suíço',
        'CNY': 'Yuan Chinês',
        'ARS': 'Peso Argentino',
        'UYU': 'Peso Uruguaio'
    }

def currency_lookup():
    print("=== CONSULTA DE COTAÇÃO DE MOEDAS ===")
    print("Consulte o valor de moedas estrangeiras em relação ao Real (BRL)")
    
    popular_currencies = get_popular_currencies()
    
    print("\nMoedas populares:")
    for code, name in popular_currencies.items():
        print(f"• {code} - {name}")
    
    while True:
        currency_input = input("\nDigite o código da moeda (ex: USD) ou 'sair' para encerrar: ").upper()
        
        if currency_input.lower() == 'sair':
            print("Consulta encerrada!")
            break
        
        if len(currency_input) != 3:
            print("❌ Código inválido! Use 3 letras (ex: USD, EUR)")
            continue
        
        print(f"Consultando cotação de {currency_input}... Aguarde...")
        currency_data = fetch_currency_info(currency_input)
        
        if currency_data:
            display_currency_info(currency_data)
        else:
            print("\n❌ Falha na consulta!")
            print("Possíveis causas:")
            print("• Moeda não encontrada ou não suportada")
            print("• Problema de conexão com a internet")
            print("• API temporariamente indisponível")
            print("\nVerifique o código da moeda e tente novamente.")

if __name__ == "__main__":
    currency_lookup()