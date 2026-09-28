# This is a Moderate User Experience Survey
# Python Procedural Exercise

In this exercise, I have trained how to apply for and while iterations.

# Important observations:

i) The for iteration is set to 50 surveys. But, the print ("Participante", i) line was added to count the number of participants and also print the number on the screen for the user to know homw many surveys have been complete until the limit 0f 50 is achieved.

ii) There have been many commands used here. But, the main ones are the nested while iterations within the for. Also, the nested if +elif conditional within the while, within the for.

iii) There have been many guards added to stop ages below 18 and above 120 with an if + elif command within a try+except and also, a .isdigit() if the user tries to add a number or special characters in the name area. Also, if the user tries to input anything different than the needed strings for the for iteration to count, the program will enter an infinite loop saying their input is incorrect to force them to input only the needed words for the program to continue.

iv) The variable survey = true is a control variable to work alongside the try+except Value Error if the user tries to insert an age below 18, since this surveu can only be done by adults.

v) Finally, added an if command to force the user to decide to stop the iteration if they don't want to continue.

# Basic instructions on how to run the program:

 - The program itself is a bit complex with its nested iterations, but, once it is running, the commands are quite simple:

a) The user inputs the name;

b) Then the age;

c) Then, the program will ask for their contribution to the survey based on their experience;

d) The program finally asks if they want to continue or not;

e) If they input the value "2", the program ends and the for iteration counts the answers, presenting them to the user.

Below is the logic pathway of the code:

```text
                    ┌─────────────────────────┐
                    │      FOR i in range     │
                    │        (1, 51)          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │  New participant │
                       └────────┬─────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │       WHILE True        │
                    │      (validate name)    │
                    └────────────┬────────────┘
                                 │
                           Is name valid?
                          ┌──────┴──────┐
                        NO             YES
                         │               │
                         ▼               ▼
                   Show error       EXIT WHILE
                         │               │
                         └───────┐       │
                                 │       ▼
                                 │  ┌──────────────────┐
                                 │  │    WHILE True    │
                                 │  │  (validate age)  │
                                 │  └────────┬─────────┘
                                 │           │
                                 │      Is age valid?
                                 │      ┌────┴────┐
                                 │     NO        YES
                                 │      │          │
                                 │      ▼          ▼
                                 │  Show error  EXIT WHILE
                                 │      │          │
                                 │      └────┐     │
                                 │           │     ▼
                                 │           │  Is age < 18?
                                 │           │   ┌────┴────┐
                                 │           │  YES        NO
                                 │           │   │          │
                                 │           │   ▼          ▼
                                 │           │  END      Continue
                                 │           │  SURVEY    survey
                                 │           │              │
                                 │           │              ▼
                                 │           │     ┌──────────────────┐
                                 │           │     │    WHILE True    │
                                 │           │     │ (validate answer)│
                                 │           │     └────────┬─────────┘
                                 │           │              │
                                 │           │        Is answer valid?
                                 │           │        ┌─────┴─────┐
                                 │           │       NO          YES
                                 │           │        │            │
                                 │           │        ▼            ▼
                                 │           │   Show error     Count answer
                                 │           │        │            │
                                 │           │        │          BREAK
                                 │           │        │            │
                                 │           │        └──────┐     │
                                 │           │               │     ▼
                                 │           │               │  Continue
                                 │           │               │  FOR loop
                                 │           │               │     │
                                 │           │               │     ▼
                                 │           │               │ Ask:
                                 │           │               │ Continue?
                                 │           │               │
                                 │           │               │   ┌──────┴──────┐
                                 │           │               │   │             │
                                 │           │               │  YES           NO
                                 │           │               │   │             │
                                 │           │               │   ▼             ▼
                                 │           │               │ Next          BREAK
                                 │           │               │ iteration        │
                                 │           │               │   │             │
                                 └───────────────────────────┘   │             ▼
                                                                 │            END
                                                                 ▼
                                                           Next participant
```

And the simplified logic:

```text
FOR
│
│  "How many participants?"
│
├── WHILE (name)
│     │
│     └── "Is the name valid?"
│
├── WHILE (age)
│     │
│     └── "Is the age valid?"
│
└── WHILE (answer)
      │
      └── "Is the answer valid?"
```

<div style="display: inline_block"><br>
<image align="center" alt = "PGhelfi-Py" height = "30" width = "40" src = "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>
