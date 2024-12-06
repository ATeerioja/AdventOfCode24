with open('6/input.txt', 'r') as file:
  completeMap = file.read().split("\n")
  fullMap = []
  for i in completeMap:
    fullMap.append(list(i))

state = "^"
paths = []

def getGuardPosition():
  for i in fullMap:
    try:
      guardPosition = (fullMap.index(i),i.index(state))
    
    except:
      continue

    else:
      return guardPosition
  
  return()

def getNextStep(position):
  if(state == "^"):
    return(position[0] - 1,position[1])
  
  if(state == "v"):
    return(position[0] + 1,position[1])
  
  if(state == "<"):
    return(position[0],position[1] - 1)
  
  if(state == ">"):
    return(position[0],position[1] + 1)
  
  return()

def move(position, next):
  
  if(state == "^" or state == "v"):
    fullMap[position[0]][position[1]] = "|"
    fullMap[next[0]][next[1]] = state

  if(state == "<" or state == ">"):
    fullMap[position[0]][position[1]] = "-"
    fullMap[next[0]][next[1]] = state
  

edge = False
loop = 0

while True:

  position = getGuardPosition()
  next = getNextStep(position)
  paths.append(position)

  try:
    if(next[0] < 0 or next[1] < 0):
      raise IndexError
    
    if(fullMap[next[0]][next[1]] == "O"):
      print("loop")
      loop += 1
      edge = True
      break


    if(fullMap[next[0]][next[1]] == "#"):
      if(state == "^"):
        state = ">"
  
      elif(state == "v"):
        state = "<"
  
      elif(state == "<"):
        state = "^"
  
      elif(state == ">"):
        state = "v"
      
      tempNext = getNextStep(position)
      fullMap[position[0]][position[1]] = "O"
      fullMap[tempNext[0]][tempNext[1]] = state
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
  calc += i.count("X")

filteredPaths = []
for i in paths:
  if i not in filteredPaths:
    filteredPaths.append(i)

filteredPaths.pop(0)

print(loop)

loop = 0
calc = 0

for i in filteredPaths:
  calc += 1
  print(f"{calc} / {len(filteredPaths)}")

  fullMap = []
  state = "^"
  for x in completeMap:
    fullMap.append(list(x))

  fullMap[i[0]][i[1]] = "#"


  loopcounter = 0


  edge = False
  while True:
    position = getGuardPosition()
    next = getNextStep(position)
    paths.append(position)

    try:
      if(next[0] < 0 or next[1] < 0):
        raise IndexError
      
      if(fullMap[next[0]][next[1]] == "O"):
        loopcounter += 1
        print("Ehkä looppaa")
        if loopcounter > 10:
          loop += 1
          edge = True
          break

      if(loopcounter > 10):
        loop += 1
        edge = True
        break


      if(fullMap[next[0]][next[1]] == "#"):
        if(state == "^"):
          state = ">"
    
        elif(state == "v"):
          state = "<"
    
        elif(state == "<"):
          state = "^"
    
        elif(state == ">"):
          state = "v"
        
        tempNext = getNextStep(position)
        if(fullMap[tempNext[0]][tempNext[1]] == "#"):
          if(state == "^"):
            state = ">"
    
          elif(state == "v"):
            state = "<"
    
          elif(state == "<"):
            state = "^"
    
          elif(state == ">"):
            state = "v"
          
          tempNext = getNextStep(position)
          fullMap[position[0]][position[1]] = "O"
          fullMap[tempNext[0]][tempNext[1]] = state
          loopcounter += 1
        else:
          fullMap[position[0]][position[1]] = "O"
          fullMap[tempNext[0]][tempNext[1]] = state
        continue

    except IndexError:
      edge = True
      fullMap[position[0]][position[1]] = "X"
      break

    move(position, next)

    if edge == False:
      continue
    
    break

print(loop)