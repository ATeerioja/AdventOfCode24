#Challenge 1
def solve(list):
  truthList = []
  
  for i in range(len(list)):
    truthListPart = []

    for z in range(len(list[i])):
      newList = [x for x in list[i]]
      del newList[z]
      isTrue = True
      isGrowing = True

      if(int(newList[0]) - int(newList[1])) > 0:
        isGrowing = False
      
      for y in range(len(newList) - 1):
        
        if(isGrowing == True):
          if not (0 > int(newList[y]) - int(newList[y + 1]) >= -3):
            isTrue = False
        
        if(isGrowing == False):
          if not (0 < int(newList[y]) - int(newList[y + 1]) <= 3):
            isTrue = False

      truthListPart.append(isTrue)
        
    truthList.append(truthListPart)
  
  
  return(truthList)



with open('2/input.txt', 'r') as file:
  content = file.read()
  contentList = content.split("\n")
  
  newContentList = []
  

  for i in contentList:
    newContentList.append(i.split(" "))

  safe = 0 

  for i in solve(newContentList):
    if(i.count(True) > 0):
      safe += 1

  print(safe)