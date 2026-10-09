# This is a Moderate User Experience Survey
# Python Procedural Exercise

In this exercise, I have trained how to apply functions "def".

# Important observations:

i) The def commands are used only for the average calculation and the status validation.

ii) 3 input guards have been added for the name, the number and the grades with while + true loops and try + except + ValueError commands to stop the user from inputting anything (that I could think of) that might cause the program to break.

# Basic instructions on how to run the program:

 - The program itself is complex with its forth and back, but, for the user, it is simple:

a) The program starts by asking the user to input their names;

b) Then the program asks how many grades will be considered for the average calculation;

c) Then, the user inputs all the grades based on the number provided previously;

d) The program will then provide their average grade and if they passed or not;

e) The program ends.

Below is the logic pathway of the code:

## ASCII Flowchart

```text

                         ┌──────────────────────────┐
                         │          START           │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │   Display system title   │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │        WHILE True        │
                         │     (validate name)      │
                         └────────────┬─────────────┘
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
                                      │  ┌──────────────────────────┐
                                      │  │        WHILE True        │
                                      │  │  (validate grade count)  │
                                      │  └────────────┬─────────────┘
                                      │               │
                                      │       Is input a valid
                                      │       integer > 0?
                                      │         ┌─────┴─────┐
                                      │        NO           YES
                                      │        │             │
                                      │        ▼             ▼
                                      │   Show error     EXIT WHILE
                                      │        │             │
                                      └────────┘             ▼
                                                   ┌─────────────────────┐
                                                   │ Initialize          │
                                                   │ Grades_List = []    │
                                                   └──────────┬──────────┘
                                                              │
                                                              ▼
                                                   ┌─────────────────────┐
                                                   │ FOR i in range      │
                                                   │ (InputGrades)       │
                                                   └──────────┬──────────┘
                                                              │
                                                              ▼
                                                   ┌─────────────────────┐
                                                   │      WHILE True     │
                                                   │   (validate grade)  │
                                                   └──────────┬──────────┘
                                                              │
                                                     Is grade a number
                                                      between 0 and 10?
                                                        ┌─────┴─────┐
                                                       NO           YES
                                                       │             │
                                                       ▼             ▼
                                                  Show error    Add grade to
                                                       │         Grades_List
                                                       │             │
                                                       │             ▼
                                                       │        BREAK WHILE
                                                       │             │
                                                       └──────┐      │
                                                              │      ▼
                                                              │  More grades
                                                              │  to enter?
                                                              │   ┌───┴───┐
                                                              │  YES      NO
                                                              │   │        │
                                                              │   ▼        ▼
                                                              │ Next     EXIT FOR
                                                              │ grade      │
                                                              │            ▼
                                                              │  ┌──────────────────────┐
                                                              │  │ Calculate final      │
                                                              │  │ average               │
                                                              │  │ sum(Grades_List) /    │
                                                              │  │ len(Grades_List)      │
                                                              │  └──────────┬───────────┘
                                                              │             │
                                                              │             ▼
                                                              │  ┌──────────────────────┐
                                                              │  │ Validate average     │
                                                              │  └──────────┬───────────┘
                                                              │             │
                                                              │       Average >= 6?
                                                              │        ┌────┴────┐
                                                              │       YES        NO
                                                              │        │          │
                                                              │        ▼          ▼
                                                              │   APPROVED   Average >= 4?
                                                              │                 ┌─┴─┐
                                                              │                YES  NO
                                                              │                 │    │
                                                              │                 ▼    ▼
                                                              │           RECOVERY  FAILED
                                                              │                 │    │
                                                              │                 └─┬──┘
                                                              │                   │
                                                              │                   ▼
                                                              │  ┌──────────────────────────┐
                                                              │  │ Display student name,    │
                                                              │  │ registered grades,       │
                                                              │  │ final average and status  │
                                                              │  └────────────┬─────────────┘
                                                              │               │
                                                              │               ▼
                                                              │  ┌──────────────────────────┐
                                                              │  │           END            │
                                                              │  └──────────────────────────┘
```
