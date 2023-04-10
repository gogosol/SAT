# SAT Solver (Python)

This code defines a function called finish_him which takes a logical formula as input and returns whether the formula is satisfiable or unsatisfiable. The logical formula can contain conjunctions (represented by the dot "." symbol) and disjunctions (represented by the plus "+" symbol), and it can consist of variables and their negations.

The function first extracts the variables from the formula and assigns each variable a boolean value by using a dictionary called "packing". It then evaluates each clause in the formula by substituting the boolean values of the variables in that clause, and stores the result in a dictionary called "veracidade".

Next, the function checks if there are any clauses that evaluate to False. If there is a variable that can be assigned a value to make a False clause True, it assigns the variable the necessary value and updates packing accordingly.

Finally, the function constructs a string that represents the formula with the boolean values of the variables substituted in, and evaluates this string to determine whether the formula is satisfiable or unsatisfiable. If the formula is satisfiable, the function returns the values of the variables that make the formula True. Otherwise, it returns "- Unsatisfiable".
