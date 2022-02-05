def arithmetic_arranger(problems, resolve=False):
  if (len(problems) > 5): 
    print("Error: Too many problems.")
    return
  output = "\n\n\n" if resolve else "\n\n"
  for problem in problems:
    output = output.split('\n')
    problem = problem.split()

    if (not problem[0].isdigit() or not problem[2].isdigit()):
      print("Error: Numbers must only contain digits.")
      return
    if (not problem[1] == '+' and not problem[1] == '-'):
      print("Error: Operator must be '+' or '-'.")
      return
    
    longest_number = len(max(problem))
    if (longest_number > 4) :
      print("Error: Numbers cannot be more than four digits.")
      return
    
    for s in range(longest_number +  2 - len(problem[0])):
      output[0] += " "
    output[0] += problem[0] + "\t"

    output[1] += problem[1]
    for s in range(longest_number +  1 - len(problem[2])):
      output[1] += " "
    output[1] += problem[2] + "\t"

    for s in range(longest_number +  2):
      output[2] += "-"
    output[2] += "\t"
    
    if (resolve):
      result = int()
      if (problem[1] == "+"):
        result += (int(problem[0]) + int(problem[2]))
      else:
        result += (int(problem[0]) - int(problem[2]))
      for s in range(longest_number +  2 - len(str(result))):
        output[3] += " "
      output[3] += str(result) + "\t"
    output = '\n'.join(output)
  print(output)