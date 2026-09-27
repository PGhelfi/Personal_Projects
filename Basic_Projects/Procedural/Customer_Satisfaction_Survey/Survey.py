# This simple program uses the command for to extract up to 50 surveys from the user.

print ("Bem vindo ao sistema de pesquisa de satisfacao da BeeOn. \n Escreva abaixo o seu nome, idade e, em seguida, escreva a sua opiniao sobre o nosso sistema de gerenciamento.")

#These variables are outside the for iteration so they are not created 50 times, which would mean that they will be resetted everytime the for iteration restarts, which would break the program. The survey variable was created as True the same way as the other varibales were created at 0, so que program understands that the initial value of the variable within the if conditional at line 35 is true and the program can continue.
Excelente = 0
Bom = 0
Ruim = 0
Survey = True

# Initial input area. The user inputs their names and their age. The try+except command then alerts the user if they have inputted anything other than a string, or, after anything other than an int.

for i in range (1, 51):

    print ("---------------------------------------------------------------------------")

    # That for starts at 0 and goes up to 49. But, that would not be natural for the user. So, we added in range (1, 51) so the count starts at 1 and goes to 50 in the result. The print below then shows the number of participants in the survey.

    print ("Participante", i)

    while True:

        Nome = input("\n Digite o seu nome: ").strip()

        if Nome.isdigit():
            print ("Nome invalido. Por favor, insira um nome valido.")
        else:
            break

    while True:
        try:
            Idade = int(input("\n Digite a sua idade: "))

            if Idade < 18:
                print ("Voce é menor de idade não pode participar da pesquisa. Procure a ajuda de um adulto.")
                Survey = False # This is a control variable to check if the user is under 18. If they are, the for iteration stops with the break.
                break
            elif Idade >= 120:
                print ("Idade invalida. Insira uma idade valida.")
            else:
                break

        except ValueError:
            print ("Idade invalida. Insira uma idade valida.")

    if Survey == False: # This will then check if the control variable turns False. If it does, the following message stops the for iteration and ends the program.
        print ("Pesquisa encerrada.")
        break
    
    # After those two validations, the user then inputs their view of experience with the product. This while + true validation is here to keep the if + elif going until the user inputs the correct wordings for the iteration to continue normally.

    print("Agora, escolha entre 'Excelente', 'Bom' ou 'Ruim' para registrar a sua experiencia com o nosso sistema empresarial.")

    while True:
        Answer = input("\n Digite a sua resposta: ").strip().lower()

        if Answer == "excelente":
            Excelente += 1
            break
        elif Answer == "bom":
            Bom += 1
            break
        elif Answer == "ruim":
            Ruim += 1
            break
        else:
            print("Resposta invalida. Digite apenas 'Excelente', 'Bom' ou 'Ruim'.")

    # This following variable asks the user if the want to continue answering the survey or not, this does not drag it unecessarily.
    Continue = input("\n Deseja realizar outra pesquisa? (1 = Sim / 2 = Não): ")

    if Continue == "2":
        break

# Output: the program then resolves all the surveys done and presents the user with the counting of each option.

print ("Excelente", Excelente)
print ("Bom", Bom)
print ("Ruim", Ruim)
