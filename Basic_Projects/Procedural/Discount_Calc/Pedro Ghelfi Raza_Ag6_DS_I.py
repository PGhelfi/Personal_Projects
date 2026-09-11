# Simple procedural discount calculator for an item being purchased based on a price variation.

# Discount variables to be applied based on the given price variation inputted.
DiscountLow = 0.05
DiscountMid = 0.10
DiscountHigh = 0.15

# User inputs the item and its price.
Product = input("Qual o produto que voce levara hoje?: ")

try:
    PriceVariation = float(input(f"\n Por favor, insira o preco de {Product} para ser ser calculado o desconto: "))

# Discount is checked, based on the low, mid, high discount criteria.
    if PriceVariation < 200:
        Discount = DiscountLow
        
    elif PriceVariation >= 200 and PriceVariation < 300:
        Discount = DiscountMid
        
    elif PriceVariation >= 300:
        Discount = DiscountHigh
    
    # Now, the discount is calculated based on the price ratio and presented to the user:
    DiscountValue = PriceVariation * Discount
    FinalPrice = PriceVariation - DiscountValue

    print (f"\n O Preco inical do item {Product} era de: R$ {PriceVariation: .2f} | "
    f" O desconto de {Discount * 100: .0f}% foi aplicado | " f"O preco final e de R$ {FinalPrice: .2f}" )
    
except ValueError:
    print ("Nenhum valor foi inserido. Fim do programa!")
