# Input - Usuario inserira o Tipo do produto e, apos, o consumo em Watts e o tempo de uso em horas.

print ("\n Esta e uma calculadora para determinar o consumo energetico de seu eletrodomestico ou eletronico.")

Tipo = input("\n Para comercarmos, digite o nome do seu eletrodomestico ou eletronico: ")

Watts = int(input("\n Digite o consumo de Watts por hora do aparelho: "))

Uso = int(input(f"\n Agora, digite quantas horas por dia voce usa {Tipo}: "))

#Variavel de calculo de consumo mensal baseado nas informacoes informadas pelo usuario.

ConsumoMensal = ((Watts * (Uso * 30)) / 1000)

# Output - Saida de dados, informando o conduso mensal do produto informado.

print (f"\n Para o produto informado {Tipo}, considerando o consumo {Watts}W e o uso diario informado de {Uso} horas, o consumo mensal e de {ConsumoMensal}KWh.")

print ("\n -------------------------------------------------------")

Escolha = int(input(f"\n Voce gostaria de saber o custo mensal do consumo de {Tipo}? Digite '1' para sim e '2' para nao: "))

# Ponro condicional, caso o usuario escolha por prosseguir com calculo adicional.

if (Escolha==1):

    CustoPorHora = float(input(" \n Digite o custo por KWh em reais. Inclua centavos, se aplicavel e uso pontos, nao virgulas para separar os centavos: "))
    
    CustoMensal = round(ConsumoMensal * CustoPorHora, 2)
    
    print (f"\n O custo mensal de {Tipo}, com consumo de {ConsumoMensal}W, usando {Uso} horas ao custo de R${CustoPorHora} gerara um custo mensal de R${CustoMensal}.")
    
    print ("\n Agradecemos o uso da calculadora de consumo e custo de eletronicos")
    
elif (Escolha==2):
        
    print ("\n Programa encerrado pelo usuario. Volte sempre!")
