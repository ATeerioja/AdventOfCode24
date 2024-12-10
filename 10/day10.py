with open("10/input.txt", "r") as file:
  data = file.read()

  trailMap = data.split("\n")

  trailMapMatrix = []
  for i in trailMap:
    trailMapMatrix.append(list(i))
  
startingLocations = []

loops = 0

for i in range(len(trailMapMatrix)):
  for x in range(len(trailMapMatrix[i])):
    if trailMapMatrix[i][x] == "0":
      startingLocations.append((i, x))

def checkBranches(data):
  start = data[0]
  step = data[1]

  branches = []
  newStep = step

  #Check if in matrix
  if not start[0] - 1 < 0 and trailMapMatrix[start[0] - 1][start[1]] == str(step + 1) :
    branches.append((start[0] - 1,start[1]))
    newStep = step + 1

  if not start[1] + 1 >= len(trailMapMatrix[0]) and  trailMapMatrix[start[0]][start[1] + 1] == str(step + 1):
    branches.append((start[0],start[1] + 1))
    newStep = step + 1
    
  if not start[0] + 1 >= len(trailMapMatrix) and trailMapMatrix[start[0] + 1][start[1]] == str(step + 1):
    branches.append((start[0] + 1,start[1]))
    newStep = step + 1

  if not start[1] - 1 < 0 and trailMapMatrix[start[0]][start[1] - 1] == str(step + 1):
    branches.append((start[0],start[1] - 1))
    newStep = step + 1

  

  
  return ((branches, newStep))


def loop(start):
  global loops
  allBranches = checkBranches(start)

  for branch in allBranches[0]:
    next = ((branch, allBranches[1]))

    if():
      print("Empty")
      break
  

    if(allBranches[1] == 9):
      for i in allBranches[0]:
        loops += 1

      break

    loop(next)
    
 
sum = 0
for i in startingLocations:
  start = ((i, 0))
  loops = 0
  loop(start)
  print(f"{start} {loops} loops")
  sum += loops

print(sum)
  


