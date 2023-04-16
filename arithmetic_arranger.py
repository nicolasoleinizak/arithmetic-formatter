def arithmetic_arranger(problems, showResult=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        
        members = problem.split(' ')
        num1 = members[0]
        op = members[1]
        num2 = members[2]

        if op == '/' or op == '*':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num1.isnumeric() or not num2.isnumeric():
            return 'Error: Numbers must only contain digits.'
        
        result = operations[op](int(num1), int(num2))

        width = max(len(num1), len(num2))+2

        line1 += num1.rjust(width)+"    "
        line2 += (op+" "*(width-1-len(num2)) + num2).rjust(width)+"    "
        line3 += "-"*width+"    "
        line4 += str(result).rjust(width)+"    "

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + \
        "\n" + line3.rstrip()
    if (showResult):
        arranged_problems += "\n" + line4.rstrip()
    return arranged_problems


operations = {
    '+':
        lambda a, b:
            a+b,
    '-':
        lambda a, b:
            a-b,
}
