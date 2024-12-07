import itertools

def try_all_operator_combinations(numbers, answer):
    # Define the operators and their functions
    operators = {
        '+': lambda x, y: x + y,
        '||': lambda x, y: int(str(x) + str(y)),
        '*': lambda x, y: x * y,
        #'/': lambda x, y: x / y if y != 0 else None  # Handle division by zero
    }
    
    # Get all possible combinations of `len(numbers) - 1` operators
    operator_combinations = list(itertools.product(operators.keys(), repeat=len(numbers) - 1))
    
    results = []
    
    # Apply each combination of operators to the numbers
    for operator_combo in operator_combinations:
        try:
            # Start with the first number
            result = numbers[0]
            steps = [str(numbers[0])]  # Track steps for printing
            
            # Apply each operator sequentially
            for i, operator in enumerate(operator_combo):
                result = operators[operator](result, numbers[i + 1])
                if result is None:  # Handle invalid operations like division by zero
                    break
                steps.append(int(numbers[i + 1]))
            
            if int(result) == int(answer):  # Only save valid results
                print("Found")
                results.append((steps, result))
                return results
        except Exception as e:
            # Catch unexpected errors
            print(f"Error with operator combination {operator_combo}: {e}")
    
    return results

with open('7/input.txt', 'r') as file:
  equationList = file.read().split("\n")
  
sum = 0

for i in equationList:
  equation = i.split(":")
  answer = equation[0]
  numbers = equation[1].split(" ")
  numbers.pop(0)
  newNumbers = []
  for num in numbers:
     newNumbers.append(int(num))

  combinations = try_all_operator_combinations(newNumbers, answer)
  try:
    sum += int(combinations[0][1])
  except:
    continue

print(sum)
      




