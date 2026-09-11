# Simple procedural discount calculator for an item being purchased based on a price ratio.

# Discount variables to be applied based on the given price ratio inputted.
DiscountLow = 0.05
DiscountMid = 0.10
DiscountHigh = 0.15

# User inputs the item and its price.
Product = input("Qual o produto que voce levara hoje?: ")

try:
    PriceRatio = float(input(f"\n Por favor, insira o preco de {Product} para ser ser calculado o desconto: "))

# Discount is checked, based on the low, mid, high discount criteria.
    if PriceRatio < 200:
        Discount = DiscountLow
        
    elif PriceRatio >= 200 and PriceRatio < 300:
        Discount = DiscountMid
        
    elif PriceRatio >= 300:
        Discount = DiscountHigh
    
    # Now, the discount is calculated based on the price ratio and presented to the user:
    DiscountValue = PriceRatio * Discount
    FinalPrice = PriceRatio - DiscountValue

    print (f"\n O Preco inical do item {Product} era de: R$ {PriceRatio: .2f} | "
    f" O desconto de {Discount * 100: .0f}% foi aplicado | " f"O preco final e de R$ {FinalPrice: .2f}" )
    
except ValueError:
    print ("Nenhum valor foi inserido. Fim do programa!")
