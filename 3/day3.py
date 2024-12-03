import re

#Challenge 2
with open('3/input.txt', 'r') as file:
  content = file.read()

  correctList = re.findall("mul\([0-9]{,3},[0-9]{,3}\)|don't\(\)|do\(\)", content)
  print(correctList)

  total = 0
  isRunning = True

  for i in correctList:

    if re.match("don't\(\)", i):
      isRunning = False
      print("Stopped")

    if re.match("do\(\)", i):
      isRunning = True
      print("Running")

    elif isRunning == True:
      print(i)
      start = i.index("(")
      middle = i.index(",")
      end = i.index(")")

      total += int(i[start+1:middle]) * int(i[middle+1:end])

    print(total)

  



    
      