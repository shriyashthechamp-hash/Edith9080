def calculate(a, b, operator):
 if operator == '+':
 result = a + b
 elif operator == '-':
 result = a - b
 elif operator == '*':
 result = a * b
 elif operator == '/':
 result = a / b
 else:
 result = None

 print(result)

calculate(20, 20, '+')
