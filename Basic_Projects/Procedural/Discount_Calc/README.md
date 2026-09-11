# This is a Basic Discount Calculator
# Python Procedural Exercise

In this exercise, I have trained how to apply if and elif. I have also tested the try and execpt keys with the ValueError exception class. Its objective is to calculate a discount based on a price variation.

# Important observation:
I do know that I could have simplified the if + elif operation with if+elif+else instead of the if+elif+elif with the boole operator "and", considering that the first if could have already identified that the "if PriceVariation < 200:" is false, that means that PriceVariation >= 200.

So, the simpler version would be:

if PriceVariation < 200:
    Discount = DiscountLow
elif PriceVariation < 300:
    Discount = DiscountMid
else:
    Discount = DiscountHigh

But, since this is a training exercise, I wanted to test the boolean operator anyway. Not to mention that the "longer" version makes the logic clearer.

Basic instructions on how to run the program:

a) Input the name of the product;

b) Input its price;

c) The program will check if the price is less than 200, between 200 and 300 or more than 300;

d) The program then calculates the price with its corresponding discount of 5%, 10% or 15% and then print the final value to the user.

e) In case the user types a string, two hundred for example, instead of a float, the try will the print that no value was insertend and the nd the program.

<div style="display: inline_block"><br>
<image align="center" alt = "PGhelfi-Py" height = "30" width = "40" src = "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>
