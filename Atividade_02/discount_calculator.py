product_name = "Camiseta"
original_price = 50.00
discount_percentage = 20

discount_value = original_price * (discount_percentage / 100)
final_price = original_price - discount_value

print(f"Produto: {product_name}")
print(f"Preço original: R$ {original_price:.2f}")
print(f"Desconto: {discount_percentage}%")
print(f"Valor do desconto: R$ {discount_value:.2f}")
print(f"Preço final: R$ {final_price:.2f}")