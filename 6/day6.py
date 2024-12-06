with open('6/input.txt', 'r') as file:
  completeMap = file.read().split("\n")
  fullMap = []
  for i in completeMap:
    fullMap.append(list(i))

state = "^"

def getGuardPosition():
  for i in fullMap:
    try:
      guardPosition = (fullMap.index(i),i.index(state))
    
    except:
      continue

    else:
      return guardPosition
  
  return(0,0)

def getNextStep(position):
  if(state == "^"):
    return(position[0] - 1,position[1])
  
  if(state == "v"):
    return(position[0] + 1,position[1])
  
  if(state == "<"):
    return(position[0],position[1] - 1)
  
  if(state == ">"):
    return(position[0],position[1] + 1)
  
  return(0,0)

def move(position, next):
  fullMap[position[0]][position[1]] = "X"
  fullMap[next[0]][next[1]] = state

edge = False

while True:

  position = getGuardPosition()
  next = getNextStep(position)

  try:
    if(next[0] < 0 or next[1] < 0):
      raise IndexError

    if(fullMap[next[0]][next[1]] == "#"):
      if(state == "^"):
        state = ">"
  
      elif(state == "v"):
        state = "<"
  
      elif(state == "<"):
        state = "^"
  
      elif(state == ">"):
        state = "v"
      
      fullMap[position[0]][position[1]] = state
      continue

  except IndexError:
    print("Edge")
    edge = True
    fullMap[position[0]][position[1]] = "X"
    break

  move(position, next)

  if edge == False:
    continue
  
  break

calc = 0
for i in fullMap:
  print(i)
  calc += i.count("X")

print(calc)
  