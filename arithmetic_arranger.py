def arithmetic_arranger(problems, showResult = False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    operations = {
        '+': 
            lambda a,b:
                a+b,
        '-':
            lambda a,b:
                a-b,
    }
    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        members = problem.split(' ')
        if members[1] == '/' or members[1] == '*':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if len(members[0])>4 or len(members[2])>4:
            return 'Error: Numbers cannot be more than four digits.'
        if not members[0].isnumeric() or not members[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        result = operations[members[1]](int(members[0]), int(members[2]))

        width = max(len(members[0]), len(members[2]))+2

        line1 += members[0].rjust(width)+"    "
        line2 += (members[1]+" "*(width-1-len(members[2]))+members[2]).rjust(width)+"    "
        line3 += "-"*width+"    "
        line4 += str(result).rjust(width)+"    "
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if(showResult):
        arranged_problems += "\n" + line4.rstrip()
    return arranged_problems