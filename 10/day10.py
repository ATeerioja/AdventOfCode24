with open("10/input.txt", "r") as file:
  data = file.read()

  trailMap = data.split("\n")

  trailMapMatrix = []
  for i in trailMap:
    trailMapMatrix.append(list(i))
  
startingLocations = []

for i in range(len(trailMapMatrix)):
  for x in range(len(trailMapMatrix[i])):
    if trailMapMatrix[i][x] == "0":
      startingLocations.append((i, x))
    
for i in startingLocations:
  start = i
  step = 0

  while True:
    print(start)
    print(step)

    try:
      if(start[0] - 1 < 0 or start[1] - 1 < 0):
        if trailMapMatrix[start[0] - 1][start[1]] == str(step + 1):
          start = ((start[0] - 1),(start[1]))
          step += 1

        if trailMapMatrix[start[0]][start[1] - 1] == str(step + 1):
          start = ((start[0]),(start[1] - 1))
          step += 1

      if trailMapMatrix[start[0]][start[1] + 1] == str(step + 1):
        start = ((start[0]),(start[1] + 1))
        step += 1
      
      if trailMapMatrix[start[0] + 1][start[1]] == str(step + 1):
        start = ((start[0] + 1),(start[1]))
        step += 1

      if(trailMapMatrix[start[0]][start[1]]) == "9":
        print("Found a Trail")
        break

    except IndexError:
      print("Index out of bounds")
      break
