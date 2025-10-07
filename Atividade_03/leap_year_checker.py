year = int(input("Digite um ano: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "é bissexto"
else:
    result = "não é bissexto"

print(f"O ano {year} {result}.")