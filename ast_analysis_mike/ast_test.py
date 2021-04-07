import ast

def simpe_eval(a):
  code = ast.parse(a)
  print(ast.dump(code,indent=2))

if __name__ == "__main__":
  simpe_eval(input("Enter regular expression: "))
