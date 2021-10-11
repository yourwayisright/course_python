import calc

calculation = input()

if calculation[1] == '+':
    result = calc.sum(x=int(calculation[0]), y=int(calculation[2]))
    print(result)

if calculation[1] == '-':
    result = calc.substruction(x=int(calculation[0]), y=int(calculation[2]))
    print(result)

if calculation[1] == '/':
    result = calc.division(x=int(calculation[0]), y=int(calculation[2]))
    print(result)

if calculation[1] == '*':
    result = calc.multiplication(x=int(calculation[0]), y=int(calculation[2]))
    print(result)
