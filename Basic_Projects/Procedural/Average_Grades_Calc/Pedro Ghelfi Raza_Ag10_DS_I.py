# Grades_Average_Calc program.

# These are the functions that will be summoned when calculating the average grades and presenting the results.

# This function below stores the average calculation.
def Grade_Len (Grades):
    if len (Grades) == 0:
        print ("Nenhum numero de medias para ser calculada a media. Insira a quantidade de notas que devam ser calculadas.")
        return 0
    return sum (Grades) / len (Grades)

# This other function stores the result based on the grades calculated. If the average is higher than 6, the student passed; if the average is between 4 and 6, they must do a test to improve their grades. If not, the student did not pass.
def Validate_Average (Average):
    if Average >= 6.0:
        return "Aprovado(a)"
    elif Average >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado(a)"

# Input area. The program acquires the amount of grades to be calculated and then stores the number in a list.
print ("Sistema de calculo de media de notas escolares.")

while True:
    Name = input("\n Digite o seu nome: ").strip()
    if Name.replace(" ", "").isalpha(): # The command isalpha(): validates if the string inputted comes from the alphabet, but it returns false if the string contains spaces. For that, the command .replace() is used, only fo the purpose of the validation, to remove spaces " " for no spaces "".
        break
    
    print("Nome inválido! Por favor, digite apenas letras.")

while True:
    try:
        InputGrades = int(input("Quantas notas deseja cadastrar? "))
        if InputGrades <= 0:
            print("Por favor, digite um número maior que zero.")
            continue
        break

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

# This list stores the grades the studen inputs.
Grades_List = []

#This iteration then populates the list above to be used by the function and calculate the average grade.
for i in range(InputGrades):
    while True:
        try: # This try+except command stops the user from inputting a text, like "I don't know", which would break the program.
            Grade = float(input(f"Insira a nota {i + 1}: "))
            
            if 0 <= Grade <= 10:
                Grades_List.append(Grade)
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número (ex: 7.5).")

FinalGrade = Grade_Len (Grades_List)

Status = Validate_Average (FinalGrade)

print (f"\n{Name}, as notas registradas foram: {Grades_List}")
print (f"A sua media final foi: {FinalGrade:.1f}") # Since this is a grading system, the final grade provides only 1 decimal for a better visualization.
print (f"\n {Name}, voce esta {Status}")
