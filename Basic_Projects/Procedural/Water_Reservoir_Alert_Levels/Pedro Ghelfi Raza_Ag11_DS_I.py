# This is a basic code to test Libraries, such as colorama. The program receives and input from the user based on the level of the water reservoir and then prints an alert message, based on that level.

from colorama import Fore, Style, init
# This imports the libary colorama. Then, print (Fore.COLOR calls the desired color to be used and presented to the user.)
# The init command makes sure the library funcions properly.

init (autoreset=True)
# Here, this was added to activate the automatic restore of the style after a printed output with a color from the library.

# Here, the list allows the function to call the corresponding level according to the value inputted by the user.
reservoir_input = ["Nivel 1: Muito baixo. Critico! Verifique o reservatorio!", "Nivel 2: Nivel baixo. Atencao. Monitore a a reducao.", "Nivel 3: Nivel medio. Situacao normal.", "Nivel 4: Nivel alto. Monitore o aumento.", "Nivel 5: Nivel muito alto. Alerta! É preciso verificar o reservatorio!"]

# The function validates the inputted level from 1 to 5 and assings a color from the library whenever it is called. The internal variable "level" receives the value that was inputted afterwards when it is called by the command "alert_level = water_level (input_level)" below.
def water_level (level):
    if level == 1:
        return Fore.RED
    elif level == 2:
        return Fore.YELLOW
    elif level == 3:
        return Fore.GREEN
    elif level == 4:
         return Fore.CYAN
    elif level == 5:
         return Fore.BLUE
    else:
        return Fore.WHITE

# The input area with the while + true and try + except ValueError guards to prevent the user from inputting anything that deviates from 1 through 5.
while True:
    try:
        input_level = int(input("Digite um numero de 1 a 5: "))
        if input_level < 1 or input_level > 5:
            print("Por favor, digite um número entre 1 e 5.")
            continue
        else:
            # The variable input_level stores the value inputted by the user. Then, alert_level calls the function water_level, transfers the value inputted by the user and the funcion assigns the corresponding color, which in turn assigns the color from the function to the variable alert_level with the return command. What this means is that the structure correctly transfers the value within the function to call the correct corresponding value from it.
            alert_level = water_level (input_level)

            # The next variable, "output" calls the list and then subtracts 1 of the inputted value. This needs to be done because lists start at 0. So, if this is not so, the user inputs 1, which would need to be the "Nivel 1: Muito baixo. Critico! Verifique o reservatorio!", but instead receives the result "Nivel 2: Nivel baixo. Atencao. Monitore a a reducao." instead.
            output = reservoir_input [input_level - 1]
             
            print (alert_level + output + Style.RESET_ALL) # Here the command Sytle.RESET_ALL was added to make sure the terminal is restored to its default color after the colors from the libraries were used.
        break

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros de 1 a 5.")
