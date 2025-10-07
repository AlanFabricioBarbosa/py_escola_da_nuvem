print("Conversor de Temperatura")
print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")

temperature = float(input("Digite a temperatura: "))
source_unit = input("Digite a unidade de origem (C/F/K): ").upper()
target_unit = input("Digite a unidade de destino (C/F/K): ").upper()

if source_unit == "F":
    celsius = (temperature - 32) * 5/9
elif source_unit == "K":
    celsius = temperature - 273.15
else:
    celsius = temperature

if target_unit == "F":
    result = celsius * 9/5 + 32
elif target_unit == "K":
    result = celsius + 273.15
else:
    result = celsius

print(f"{temperature}°{source_unit} = {result:.2f}°{target_unit}")