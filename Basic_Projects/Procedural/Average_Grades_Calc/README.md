# This is a Moderate Level Code for a Water Reservoir Alert Level Message

# Python Procedural Exercise

In this exercise, I added the usage of libraries to the mix, particularly colorama.

# Important observations:

i) Added both funtions and lists to the code. The function commands the conditional path to determine the color and the list stores the messages based on the inputted value by the user.

ii) As usual, the while + True and Try + Except + ValueError guard has been added to prevent the user from inputting anything that deviates from the needed to run the code smoothly.

iii) The library colorama was used within the funciton to determine the output for the user and help identify the level of alert based on the value inputted.

# Basic instructions on how to run the program:

a) The program starts by asking the user to input the a value from 1 to 5;

b) The program automatically prints a message based on the value inputted, from Level 1: Critically Low, 2: Low, 3: Normal, 4: High and 5: Critically High.

e) The program ends.

<div style="display: inline_block"><br>
<image align="center" alt = "PGhelfi-Py" height = "30" width = "40" src = "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

Below is the logic pathway of the code:

## ASCII Flowchart

```text

          ┌────────────────────────────────────────┐
          │             [Start Program]            │
          └───────────────────┬────────────────────┘
                              │
                              ▼
          ┌────────────────────────────────────────┐
          │  Import Colorama & Define Messages     │
          └───────────────────┬────────────────────┘
                              │
                              ▼
          ┌────────────────────────────────────────┐
          │              while True:               │ ◄── [MAIN LOOP]
          └───────────────────┬────────────────────┘
                              │
                              ▼
          ┌────────────────────────────────────────┐
          │     try: Read user input               │ ◄── [ERROR BLOCK]
          └───────────────────┬────────────────────┘
                              │
                    Did ValueError occur?
                    ├──► YES ──► ┌────────────────────────────────────────┐
                    │            │ Print invalid value error message      │ ──┐
                    │            └────────────────────────────────────────┘   │
                    └──► NO                                                  │
                              │                                               │
                              ▼                                               │
          ┌────────────────────────────────────────┐                          │
          │    if input_level < 1 or > 5?          │ ◄── [CONDITIONAL]        │
          └───────────────────┬────────────────────┘                          │
                    ├──► YES ──► ┌────────────────────────────────────────┐   │
                    │            │ Print range warning & `continue`       │ ──┘
                    │            └────────────────────────────────────────┘   │
                    └──► NO                                                  │
                              │                                               │
                              ▼                                               │
          ┌────────────────────────────────────────┐                          │
          │  water_level(input_level) -> Color     │ ◄── [FUNCTION / CONDITIONAL]
          └───────────────────┬────────────────────┘                          │
                              │                                               │
                              ▼                                               │
          ┌────────────────────────────────────────┐                          │
          │  output = reservoir_input[input - 1]   │                          │
          └───────────────────┬────────────────────┘                          │
                              │                                               │
                              ▼                                               │
          ┌────────────────────────────────────────┐                          │
          │  Print colored alert & reset style     │                          │
          └───────────────────┬────────────────────┘                          │
                              │                                               │
                              ▼                                               │
          ┌────────────────────────────────────────┐                          │
          │          break (Exit Loop)             │ ◄── [LOOP EXIT]──────────┘
          └───────────────────┬────────────────────┘
                              │
                              ▼
          ┌────────────────────────────────────────┐
          │               [End]                    │
          └────────────────────────────────────────┘
```
