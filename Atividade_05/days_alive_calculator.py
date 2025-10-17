from datetime import datetime, date

def calculate_days_alive(birth_date):
    """
    Calcula quantos dias uma pessoa está viva.
    
    Parâmetros:
    birth_date (date): Data de nascimento
    
    Retorna:
    int: Número de dias vivos
    """
    today = date.today()
    days_alive = (today - birth_date).days
    return days_alive

def get_birth_date():
    """
    Solicita e valida a data de nascimento do usuário.
    
    Retorna:
    date: Data de nascimento válida
    """
    while True:
        try:
            print("Digite sua data de nascimento:")
            day = int(input("Dia (1-31): "))
            month = int(input("Mês (1-12): "))
            year = int(input("Ano (ex: 1990): "))
            
            birth_date = date(year, month, day)
            
            # Verifica se a data não é futura
            if birth_date > date.today():
                print("Erro: A data de nascimento não pode ser futura!")
                continue
            
            # Verifica se a pessoa não tem mais de 150 anos
            if (date.today() - birth_date).days > 150 * 365:
                print("Erro: Data muito antiga! Verifique os dados.")
                continue
            
            return birth_date
            
        except ValueError:
            print("Erro: Data inválida! Verifique os valores inseridos.")

def days_alive_calculator():
    print("=== CALCULADORA DE DIAS DE VIDA ===")
    print("Descubra há quantos dias você está vivo!")
    
    while True:
        birth_date = get_birth_date()
        days_alive = calculate_days_alive(birth_date)
        
        # Cálculos adicionais
        years_alive = days_alive // 365
        months_alive = days_alive // 30
        weeks_alive = days_alive // 7
        hours_alive = days_alive * 24
        minutes_alive = hours_alive * 60
        
        today = date.today()
        age_years = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age_years -= 1
        
        print("\n" + "="*50)
        print("RELATÓRIO DE VIDA")
        print("="*50)
        print(f"Data de nascimento: {birth_date.strftime('%d/%m/%Y')}")
        print(f"Data atual: {today.strftime('%d/%m/%Y')}")
        print(f"Idade: {age_years} anos")
        print(f"\nTempo de vida:")
        print(f"• {days_alive:,} dias")
        print(f"• {weeks_alive:,} semanas")
        print(f"• {months_alive:,} meses (aproximadamente)")
        print(f"• {hours_alive:,} horas")
        print(f"• {minutes_alive:,} minutos")
        print("="*50)
        
        # Próximo aniversário
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        
        days_to_birthday = (next_birthday - today).days
        print(f"Próximo aniversário: {next_birthday.strftime('%d/%m/%Y')}")
        print(f"Faltam {days_to_birthday} dias para seu aniversário!")
        
        another = input("\nDeseja calcular para outra pessoa? (s/n): ")
        if another.lower() != 's':
            print("Obrigado por usar a calculadora de dias de vida!")
            break

if __name__ == "__main__":
    days_alive_calculator()