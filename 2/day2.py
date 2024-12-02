#Challenge 1
with open('2/input.txt', 'r') as file:
  content = file.read()
  contentList = content.split("\n")
  
  newContentList = []

  for i in contentList:
    newContentList.append(i.split(" "))

  safe = 0

  for x in newContentList:
    isTrue = -1
    isIncreasing = True


    print(x)
    for y in range(len(x) - 1):
      if y == 0:
        if (int(x[y]) - int(x[y + 1]) > 0):
          isIncreasing = False

      if isIncreasing == False:
        if(0 < int(x[y]) - int(x[y + 1]) <= 3):
          isTrue += 1
        elif(y != (len(x) -2 ) and 0 < int(x[y]) - int(x[y + 1]) <= 3):
          isTrue += 1

      if isIncreasing == True:
        if(-3 <= int(x[y]) - int(x[y + 1]) < 0):
          isTrue += 1
        elif(y != (len(x) -2 ) and -3 <= int(x[y]) - int(x[y + 1]) < 0):
          isTrue += 1

      if(y == isTrue and y == (len(x) - 2)):
        safe += 1
        print(safe)
      
  print(safe)
    

  