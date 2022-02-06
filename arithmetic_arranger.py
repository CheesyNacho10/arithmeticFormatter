def arithmetic_arranger(problems, resolve=False):
  if (len(problems) > 5): 
    return "Error: Too many problems."
    
  output = "\n\n\n" if resolve else "\n\n"
  for problem in problems:
    output = output.split('\n')
    problem = problem.split()

    if (not problem[0].isdigit() or not problem[2].isdigit()):
      return "Error: Numbers must only contain digits."
    if (not problem[1] == '+' and not problem[1] == '-'):
      return "Error: Operator must be '+' or '-'."

    longest_number = len(max(problem, key=len))
    if (longest_number > 4) :
      return "Error: Numbers cannot be more than four digits."
    
    for s in range(longest_number +  2 - len(problem[0])):
      output[0] += " "
    output[0] += problem[0]

    output[1] += problem[1]
    for s in range(longest_number +  1 - len(problem[2])):
      output[1] += " "
    output[1] += problem[2]

    for s in range(longest_number +  2):
      output[2] += "-"
    
    if (resolve):
      result = int()
      if (problem[1] == "+"):
        result += (int(problem[0]) + int(problem[2]))
      else:
        result += (int(problem[0]) - int(problem[2]))
      for s in range(longest_number +  2 - len(str(result))):
        output[3] += " "
      output[3] += str(result) + "    "
    else :
      output[2] += "    "
    
    output = '    \n'.join(output)

  output = output.split('\n')
  for l in range(len(output)):
    output[l] = output[l].rstrip()
  output = '\n'.join(output)
  return output