def arithmetic_arranger(problems, answer = False):

    s = problems;   
    t = ' '.join(problems);
    u = t.split();

    #Conditional statements for number of problems constraint
    if len(u) > 15:
        return "Error: Too many problems.";
        
    
    #Conditional statements to look for + or - operators
    for n in u:
        if n == "*" or n == "/":
            return "Error: Operator must be '+' or '-'.";


    #Conditional statement to make sure all values entered are digits and contain no letters
    for x in range(0, len(u)):
        if x == 1 or x == 4 or x == 7 or x == 10 or x == 13:
            continue;
        if u[x].isdigit():
            continue;
        else:
            return "Error: Numbers must only contain digits.";

     #Conditional statement for length of numbers
    for item in u:
        if len(item) <= 4:
            continue;
        else:
            return "Error: Numbers cannot be more than four digits.";

    #Formatting the outputs
    line1 = "";
    line2 = "";
    line3 = "";
    line4 = "";

    for problem in problems:
        num1 = problem.split(" ")[0];
        operator = problem.split(" ")[1];
        num2 = problem.split(" ")[2];

        if operator == "+":
            numsl4 = str(int(num1) + int(num2));
        elif operator == "-":
            numsl4 = str(int(num1) - int(num2));
        
        lengthl3 = max(len(num1), len(num2)) + 2;
        numsl1 = str(num1).rjust(lengthl3);
        numsl2 = operator + str(num2).rjust(lengthl3 - 1);
        dashesl3 = "-" * lengthl3;
        ans = str(numsl4).rjust(lengthl3);

        if problem != problems[-1]:
            line1 += numsl1 + "    ";
            line2 += numsl2 + "    ";
            line3 += dashesl3 + "    ";
            line4 += ans + "    ";
        else:
            line1 += numsl1;
            line2 += numsl2;
            line3 += dashesl3;
            line4 += ans;
        
    if answer == True:
        output = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4;
    else:
        output =  line1 + "\n" + line2 + "\n" + line3;

    return output;