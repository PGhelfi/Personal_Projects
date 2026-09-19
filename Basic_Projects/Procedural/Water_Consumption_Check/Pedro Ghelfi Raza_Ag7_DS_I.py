# This is simple a Water Consumption monitoring application.

# Input area. The user inputs the types, which are limited to "apartamento", "casa" or "comercial".

Building_Type = input("Escreva o tipo de imóvel a ser analisado: ").strip().lower()

# This validation stops the user if they try to input anything other than those three options below.

if Building_Type not in ("apartamento", "casa", "comercial"):
    print ("Tipo de imovel invalido. Digite um imovel compativel.")
    exit()

# And this one prevents the user to input anything that is not a float number for the consunption.

try:
    Monthly_Consumption = float(input("\n Insira agora o consumo em metros cubicos: "))
except ValueError:
    print ("Dados inválidos. Leia novamente as instrucoes e insira os dados conforme o requistado.")
    exit()

# This is the checking area, where the building data is validated and checked against a comsuption ratio to identify if the consumption is within limits or not.

match Building_Type:
    case "comercial":
            print ("O consumo será relacionado a uma conta comercial e tarifas diferentes. Consulte o plano corporativo.")
    case "apartamento" if Monthly_Consumption <10:
            print ("Consumo enconômico; Excelente controle de agua!")
    case "apartamento" | "casa" if Monthly_Consumption <=25:
            print ("Consumo moderado e esta dentro do padrão residencial.")
    case _:
            print ("O seu consumo aparenta ser excessivo. Recomendamos checagem por vazamentos e medidas de economia.")
