age = int(input("Digite sua idade: "))

if age >= 0 and age <= 12:
    category = "Criança"
elif age >= 13 and age <= 17:
    category = "Adolescente"
elif age >= 18 and age <= 59:
    category = "Adulto"
elif age >= 60:
    category = "Idoso"
else:
    category = "Idade inválida"

print(f"Idade: {age} anos")
print(f"Categoria: {category}")