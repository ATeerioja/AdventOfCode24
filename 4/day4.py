with open('4/input.txt', 'r') as file:
  content = file.read()
  contentList = content.split("\n")

  reverseContentList = []
  for i in contentList:
    reverseContentList.append(list(reversed(i)))


def horizontal(list):
  count = 0

  for i in list:
    count += i.count("XMAS")
    count += i.count("SAMX")

  return count

def vertical(list):
  count = 0
  x = 0

  while x <= len(list):
    if(x + 4 > len(list)):
      return count
    
    for i in range(len(list[0])):
      answer = list[x][i]
      answer += list[x + 1][i]
      answer += list[x + 2][i]
      answer += list[x + 3][i]
      
      if answer == "XMAS" or answer == "SAMX":
        print(f"{answer} {x} {i}")
        count += 1
    
    x += 1

  return count

def diagonal(list):
  count = 0
  
  for x in range(len(list)):
    if x + 4 > len(list):
      break

    for i in range(len(list[x]) - 3):
      answer = list[x][i]
      answer += list[x + 1][i + 1]
      answer += list[x + 2][i + 2]
      answer += list[x + 3][i + 3]
        
      if answer == "XMAS" or answer == "SAMX":
        print(f"{answer} {x} {i}")
        count += 1


  return count
v = (vertical(contentList))
h = (horizontal(contentList))
d = (diagonal(contentList))
dr = (diagonal(reverseContentList))

print(v+h+d+dr)

