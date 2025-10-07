value_reais = 100.00
dollar_rate = 5.20
euro_rate = 6.15

dollar_value = value_reais / dollar_rate
euro_value = value_reais / euro_rate

print(f"Valor em reais: R$ {value_reais:.2f}")
print(f"Taxa do dólar: R$ {dollar_rate:.2f}")
print(f"Taxa do euro: R$ {euro_rate:.2f}")
print(f"Valor em dólares: $ {dollar_value:.2f}")
print(f"Valor em euros: € {euro_value:.2f}")