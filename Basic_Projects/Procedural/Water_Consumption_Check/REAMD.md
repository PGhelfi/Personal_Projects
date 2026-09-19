# This is a Basic Water Consuption Check Program.

# Python Procedural Exercise

Its main purpose is to ask the user to input the name of the building, then the water consuption in cubic meters to validate if the consuption is acceptable, moderate or if it requires alignment.

# Some important notes:

1) Used the match + case structure alongside if instead of a simple if + elif to a) test it and b) see how it behaves.
2) Implemented 3 guards: a) a .strip() to remove any spaces before or after the string and a .lower() to force whatever the user inputs into lower case, b) an if + not in to validate if the user inputs anything that is not one of the three choices available with the exit() to continue the program after the validation and c) a try + except + ValueError also in case the user does not input a number with and exit() to continue with the program after the validations.
3) In order to make the match + case work, combined it with if and the variable related to monthly consumption.
4) The | between strings works the same way as the boolean operator OR to validate the strings within the case.

# Basic instructions on how to run the program:

a) Input the type of building, but only "apartament", "house" or "comercial building";

b) Input the water consuption in cubic meters;

c) The program then validates as being economic if under 10, moderate if under or equal to 25 and in need of alignment if higher than 25;

h) End the program with the last case_, which is used to call the output if everything else is exhausted.

<div style="display: inline_block"><br>
<image align="center" alt = "PGhelfi-Py" height = "30" width = "40" src = "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>
