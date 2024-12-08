with open('8/input.txt', 'r') as file:
  fullFile = file.read()
  
  fullMap = fullFile.split("\n")

  
  mapMatrix = []
  for i in fullMap:
    mapMatrix.append(list(i))

  towers = set(fullFile)
  not_towers = {"\n", ".", "#"}

  filteredTowers = {i for i in towers if i not in not_towers}

calc = set()

for i in filteredTowers:
  indexes = [(row_idx, col_idx) 
            for row_idx, row in enumerate(list(mapMatrix)) 
            for col_idx, char in enumerate(row) 
            if char == i]
  

  for x in indexes:
    center = x

    for z in indexes:
      if z == center:
        continue

      print(z)
      
      xDiff = z[1] - center[1]
      yDiff = z[0] - center[0]

      totalDiff = (yDiff, xDiff)


      for i in range(1,100):
        newCoordinate  = ((center[0] - yDiff) * i, (center[1] - xDiff) * i)
      

        try:
          arvo = mapMatrix[newCoordinate[0]][newCoordinate[1]] 
          if(newCoordinate[0] >= 0 and newCoordinate[1] >= 0):
            print(newCoordinate)
            calc.add(newCoordinate)
            print(f"laiton tähän yhen bossi{newCoordinate}")
        
        except:
          print("Exception")
          break

        
print(len(calc))






