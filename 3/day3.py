import re

with open('3/input.txt', 'r') as file:
  content = file.read()

  correctList = re.findall("mul\([0-9]{,3},[0-9]{,3}\)", content)

  total = 0

  for i in correctList:
    start = i.index("(")
    middle = i.index(",")
    end = i.index(")")

    total += int(i[start+1:middle]) * int(i[middle+1:end])
    print(total)



  



    
      