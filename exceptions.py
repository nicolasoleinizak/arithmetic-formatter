class TooManyProblems(Exception):
  def __init__(self):
    message =  "Error: Too many problems."
    super().__init__(message)  
  pass

class WrongOperator(Exception):
  def __init__(self):
    message =  "Error: Operator must be '+' or '-'."
    super().__init__(message) 
  
  pass

class DigitsMax(Exception):
  def __init__(self):
    message =  "Error: Numbers cannot be more than four digits."
    super().__init__(message) 
  
  pass

class NotNumeric(Exception):
  def __init__(self):
    message =  "Error: Numbers must only contain digits."
    super().__init__(message) 
  