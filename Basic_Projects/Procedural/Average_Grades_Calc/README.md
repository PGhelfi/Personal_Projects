# This is a Moderate Level Code for a Water Reservoir Alert Level Message

# Python Procedural Exercise

In this exercise, I have trained how to use funtions.

# Important observations:

i) Added both funtions and lists to the code. The function commands the needed to calculated the average. The list stores their grades to be used to calculate the averages.

ii) As usual, the while + True and Try + Except + ValueError guard has been added to prevent the user from inputting anything that deviates from the needed to run the code smoothly.

iii) The for loop populates the list. Added a guard within the loop to stop the user from inputting a grade lower than 0 or higher than 10.

# Basic instructions on how to run the program:

a) The program starts by asking the user to input their names;

c) Then, the user inputs their grades.

d) The program automatically populates the list to calculate the average grades and then calculates the average value.

e) The program presents the results.

d) The program ends.

<div style="display: inline_block"><br>
<image align="center" alt = "PGhelfi-Py" height = "30" width = "40" src = "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

Below is the logic pathway of the code:

## ASCII Flowchart

```text
+-----------------------------------------------------------------------+
|                              [ START ]                                |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                Print: "Sistema de calculo de media..."                |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                 [ LOOP BOX: Student Name Validation ]                 |
|  +-----------------------------------------------------------------+  |
|  | Input Name & apply .strip()                                     |  |
|  +-----------------------------------------------------------------+  |
|                                  │                                    |
|                                  ▼                                    |
|  +-----------------------------------------------------------------+  |
|  | DECISION: Is Name.replace(" ", "").isalpha()?                   |  |
|  +-----------------------------------------------------------------+  |
|          │ (False)                                  │ (True)          |
|          ▼                                          ▼                 |
|  +-----------------------+                   [ Break Loop ]           |
|  | Print: "Nome          |                          │                 |
|  | inválido!"            |                          │                 |
|  +-----------------------+                          │                 |
|          │                                          │                 |
|          └───────────────────┐  ┌───────────────────┘                 |
|                              ▼  ▼                                     |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                 [ LOOP BOX: Grade Count Input ]                       |
|  +-----------------------------------------------------------------+  |
|  | Try: Input integer (InputGrades)                                |  |
|  +-----------------------------------------------------------------+  |
|                                  │                                    |
|                                  ▼                                    |
|  +-----------------------------------------------------------------+  |
|  | DECISION: Is InputGrades <= 0 (or ValueError exception)?        |  |
|  +-----------------------------------------------------------------+  |
|          │ (True / Exception)                       │ (False)         |
|          ▼                                          ▼                 |
|  +-----------------------+                   [ Break Loop ]           |
|  | Print Error Message   |                          │                 |
|  +-----------------------+                          │                 |
|          │                                          │                 |
|          └───────────────────┐  ┌───────────────────┘                 |
|                              ▼  ▼                                     |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                     Initialize: Grades_List = []                      |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|            [ FOR LOOP BOX: Iterate 'i' in InputGrades ]               |
|                                                                       |
|  +-----------------------------------------------------------------+  |
|  |              [ LOOP BOX: Individual Grade Input ]               |  |
|  |  +-----------------------------------------------------------+  |  |
|  |  | Try: Input float (Grade) for index i + 1                  |  |  |
|  |  +-----------------------------------------------------------+  |  |
|  |                               │                              |  |  |
|  |                               ▼                              |  |  |
|  |  +-----------------------------------------------------------+  |  |
|  |  | DECISION: Is 0 <= Grade <= 10 (and valid float)?          |  |  |
|  |  +-----------------------------------------------------------+  |  |
|  |          │ (False / Exception)           │ (True)            |  |  |
|  |          ▼                               ▼                   |  |  |
|  |  +-----------------------+        [ Grades_List.append(Grade)|  |  |
|  |  | Print Error Message   |        [ Break Inner Loop ]       |  |  |
|  |  +-----------------------+               │                   |  |  |
|  |          │                               │                   |  |  |
|  |          └───────────────────┐  ┌────────┘                   |  |  |
|  |                              ▼  ▼                            |  |  |
|  +-----------------------------------------------------------------+  |
|                                  │                                    |
|                       [ More iterations? ]                            |
|                       (Yes) ──► [ Next 'i' in Range ]                 |
|                       (No)                                            |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                    [ FUNCTION: Grade_Len(Grades) ]                    |
|  +-----------------------------------------------------------------+  |
|  | DECISION: Is len(Grades) == 0?                                  |  |
|  +-----------------------------------------------------------------+  |
|          │ (True)                                   │ (False)         |
|          ▼                                          ▼                 |
|  +-----------------------+                  +----------------------+  |
|  | • Print warning       |                  | • Calculate:         |  |
|  | • Return 0            |                  |   sum(Grades) /      |  |
|  |                       |                  |   len(Grades)        |  |
|  |                       |                  | • Return Result      |  |
|  +-----------------------+                  +----------------------+  |
|          │                                          │                 |
|          └───────────────────┐  ┌───────────────────┘                 |
|                              ▼  ▼                                     |
|                 [ Store Result in FinalGrade ]                        |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|               [ FUNCTION: Validate_Average(FinalGrade) ]              |
|  +-----------------------------------------------------------------+  |
|  | DECISION: FinalGrade >= 6.0?                                    |  |
|  +-----------------------------------------------------------------+  |
|          │ (Yes)                                    │ (No)            |
|          ▼                                          ▼                 |
|     "Aprovado(a)"                            +-------------------+    |
|                                              | DECISION:         |    |
|                                              | FinalGrade >= 4.0?|    |
|                                              +-------------------+    |
|                                                   │ (Yes)   │ (No)    |
|                                                   ▼         ▼         |
|                                            "Recuperação" "Reprovado(a)"|
|          │                                          │                 |
|          └───────────────────┬──────────────────────┘                 |
|                              ▼                                        |
|                   [ Store Result in Status ]                          |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|      Print Results: Name, Grades_List, FinalGrade, & Status Status    |
+-----------------------------------------------------------------------+
                                   │
                                   ▼
+-----------------------------------------------------------------------+
|                               [ END ]                                 |
+-----------------------------------------------------------------------+
```
