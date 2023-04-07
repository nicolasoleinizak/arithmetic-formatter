def arithmetic_arranger(problems):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        members = problem.split(' ')
        if members[1] == '/' or members[1] == '*':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if len(members[0])>4 or len(members[2])>4:
            return 'Error: Numbers cannot be more than four digits.'
        if not members[0].isnumeric() or not members[2].isnumeric():
            return 'Error: Numbers must only contain digits.'

    arranged_problems = ''
    return arranged_problems