#Challenge 1
with open('1/input.txt', 'r') as file:
  content = file.read()
  contentTrim = content.replace("\n", "   ")
  contentList = contentTrim.split("   ")

  leftList = []
  rightList = []

  for i in range(len(contentList)):
    if(i % 2 == 0):
      leftList.append(int(contentList[i]))
    else:
      rightList.append(int(contentList[i]))


  sortedLeftList = sorted(leftList)
  sortedRightList = sorted(rightList)

  distance = 0

  for i in range(len(sortedLeftList)):
    distance += abs(sortedLeftList[i] - sortedRightList[i])
    
  print(distance)

#Challenge 2