import re

with open('5/input.txt', 'r') as file:
  content = file.read()
  contentList = content.split("\n")
  numberList = []
  correctNumberList = []
  pageList = []

  incorrect = []
  isTrue = True

for i in contentList:
    if(i == ''):
      isTrue = False
      continue

    if(isTrue == False):
      numberList.append(i)
    else:
      pageList.append(i)

for i in numberList:
  correctNumberList.append(i.split(","))

correct = []

for r in range(len(correctNumberList)):
    isCorrect = True

    for x in range(len(correctNumberList[r])):
      indiciesBefore = [i for i in range(len(pageList)) if pageList[i][0]+pageList[i][1] == correctNumberList[r][x]]
      indiciesAfter = [i for i in range(len(pageList)) if pageList[i][3]+pageList[i][4] == correctNumberList[r][x]]

      
      beforeCounter = 0
      for y in indiciesBefore:
        for z in correctNumberList[r]:
          if(z == pageList[y][3]+pageList[y][4]):
            beforeCounter += 1
    
      if(beforeCounter < len(correctNumberList[r]) - x - 1):
        isCorrect = False
        incorrect.append(correctNumberList[r])
        break

      for y in indiciesAfter:
        for z in range(len(correctNumberList[r]) - x - 1):
          if(correctNumberList[z] == pageList[y][0]+pageList[y][1]):
            isCorrect = False
            incorrect.append(correctNumberList[r])
            break

    if(isCorrect):
      correct.append(r)

sum = 0
for x in correct:

    input_list = correctNumberList[x]

    middle = float(len(input_list))/2
    if middle % 2 != 0:
        sum += int(input_list[int(middle - .5)])
    else:
        sum += int((input_list[int(middle)], input_list[int(middle-1)]))

for r in range(len(incorrect)):
  print(f"{r} / {len(incorrect)}")
  for x in range(len(incorrect[r])):

    indiciesBefore = [i for i in range(len(pageList)) if pageList[i][0]+pageList[i][1] == incorrect[r][x]]
    
    for x in range(len(incorrect[r])):
      indiciesAfter = [i for i in range(len(pageList)) if pageList[i][3]+pageList[i][4] == incorrect[r][x]]
      for i in indiciesAfter:
        try:
          if (incorrect[r].index(pageList[i][0]+pageList[i][1]) > incorrect[r].index(pageList[i][3]+pageList[i][4])):
            
            first = incorrect[r].index(pageList[i][0]+pageList[i][1])
            second = incorrect[r].index(pageList[i][3]+pageList[i][4])

            temp = incorrect[r][second]
            incorrect[r][second] = incorrect[r][first]
            incorrect[r][first] = temp

        finally:
          continue
         
    beforeCounter = 0
    for y in indiciesBefore:
      for z in incorrect[r]:
        if(z == pageList[y][3]+pageList[y][4]):
         beforeCounter += 1
    
    if(beforeCounter < len(incorrect[r]) - x - 1):
      print("False")   
    

summa = 0
for x in range(len(incorrect)):

    input_list = incorrect[x]

    middle = float(len(input_list))/2
    if middle % 2 != 0:
        summa += int(input_list[int(middle - .5)])
    else:
        summa += int((input_list[int(middle)], input_list[int(middle-1)]))



      

