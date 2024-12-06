with open('6/input.txt', 'r') as file:
  completeMap = file.read().split("\n")
  fullMap = []
  for i in completeMap:
    fullMap.append(list(i))


start = (0,0)

for i in range(len(fullMap)):
  for x in range(len(fullMap[i])):
    if(fullMap[i][x] == "^"):
      start = (i,x)

currentPos = start
status = "^"

def moveUp():
  return (currentPos[0] - 1, currentPos[1])

def moveDown():
  return (currentPos[0] + 1, currentPos[1])

def moveLeft():
  return (currentPos[0], currentPos[1] - 1)

def moveRight():
  return (currentPos[0], currentPos[1] + 1)


def tryMove():
  nextMove = (0,0)

  if status == "^":
    nextMove = moveUp()

  if status == "v":
    nextMove = moveDown()

  if status == "<":
    nextMove = moveLeft()

  if status == "^":
    nextMove = moveRight()

  try:
    nextSpace = fullMap[nextMove[0]][nextMove[1]]

  except:
    print("Exception")

  else:
    if nextSpace == "#":
        if status == "^":
    nextMove = moveUp()

  if status == "v":
    nextMove = moveDown()

  if status == "<":
    nextMove = moveLeft()

  if status == "^":
    nextMove = moveRight()
  

  