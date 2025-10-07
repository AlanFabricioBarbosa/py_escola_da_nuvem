def get_valid_weight():
    while True:
        try:
            weight = float(input("Digite seu peso (em kg): "))
            if weight <= 0:
                print("Erro: O peso deve ser maior que zero.")
                continue
            if weight > 500:
                print("Erro: Peso muito alto. Digite um valor válido.")
                continue
            return weight
        except ValueError:
            print("Erro: Digite um número válido para o peso.")

def get_valid_height():
    while True:
        try:
            height = float(input("Digite sua altura (em metros): "))
            if height <= 0:
                print("Erro: A altura deve ser maior que zero.")
                continue
            if height > 3.0:
                print("Erro: Altura muito alta. Digite um valor válido.")
                continue
            if height < 0.5:
                print("Erro: Altura muito baixa. Digite um valor válido.")
                continue
            return height
        except ValueError:
            print("Erro: Digite um número válido para a altura.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_classification(bmi):
    if bmi < 18.5:
        return "Abaixo do peso", "🔵"
    elif bmi < 25:
        return "Peso normal", "🟢"
    elif bmi < 30:
        return "Sobrepeso", "🟡"
    elif bmi < 35:
        return "Obesidade grau I", "🟠"
    elif bmi < 40:
        return "Obesidade grau II", "🔴"
    else:
        return "Obesidade grau III (mórbida)", "🔴"

def get_health_recommendation(classification):
    recommendations = {
        "Abaixo do peso": "Consulte um nutricionista para ganhar peso de forma saudável.",
        "Peso normal": "Parabéns! Mantenha seus hábitos saudáveis.",
        "Sobrepeso": "Considere uma dieta equilibrada e exercícios regulares.",
        "Obesidade grau I": "Procure orientação médica para um plano de emagrecimento.",
        "Obesidade grau II": "É importante buscar acompanhamento médico especializado.",
        "Obesidade grau III (mórbida)": "Procure urgentemente um médico especialista."
    }
    return recommendations.get(classification, "Consulte um profissional de saúde.")

def main():
    print("=" * 50)
    print("🏥 CALCULADORA DE IMC (Índice de Massa Corporal)")
    print("=" * 50)
    
    weight = get_valid_weight()
    height = get_valid_height()
    
    bmi = calculate_bmi(weight, height)
    classification, emoji = get_bmi_classification(bmi)
    recommendation = get_health_recommendation(classification)
    
    print("\n" + "=" * 50)
    print("📊 RESULTADO")
    print("=" * 50)
    print(f"Peso: {weight} kg")
    print(f"Altura: {height} m")
    print(f"IMC: {bmi:.1f}")
    print(f"Classificação: {emoji} {classification}")
    print(f"\n💡 Recomendação: {recommendation}")
    print("=" * 50)
    
    print("\n📋 Tabela de Referência IMC:")
    print("• Abaixo de 18,5: Abaixo do peso")
    print("• 18,5 - 24,9: Peso normal")
    print("• 25,0 - 29,9: Sobrepeso")
    print("• 30,0 - 34,9: Obesidade grau I")
    print("• 35,0 - 39,9: Obesidade grau II")
    print("• Acima de 40,0: Obesidade grau III")

if __name__ == "__main__":
    main()