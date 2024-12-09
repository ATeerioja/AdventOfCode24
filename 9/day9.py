with open("9/input.txt", "r") as file:
  data = file.read()

  memory = {}

  index = 0
  for i in range(len(data)):
    if i % 2 == 0:
      memory[index] = (index, int(data[i]))
      index += 1


  calc = 0
  line = []
  for i in range(len(data)):
    tempLine = []
    if i % 2 == 0:

      for z in range(memory[calc][1]):
        tempLine.append(str(memory[calc][0]))

      calc += 1

    else:
      for z in range(int(data[i])):
        tempLine.append(".")

    line.append(tempLine)

changed = set()

for rev in reversed(range(len(line))):
  print(f"{rev} / {len(line)}")
  try:
    newLine = ""
    
    if(line[rev][0] in changed):
      continue

    if(line[rev][0] != "."):
      changed.add(line[rev][0])
      spaceReq = len(line[rev])

      for i in range(rev):

        if(line[i].count(".") >= spaceReq):
          length = 0

          for x in range(len(line[i])):
            if length >= spaceReq:
              raise Exception("End")
            
            if(line[i][x] == "."):
              line[i][x] = line[rev][length]
              line[rev][length] = "."
              length += 1
          
          break

            

  except:
    continue

print(line)

sum = 0
calc = 0

newLine = ""
for i in line:
  for x in i:
    newLine += x

print(newLine)
  

for i in range(len(line)):
  for x in range(len(line[i])):
    if line[i][x] == ".":
      calc += 1
      continue

    sum += int(line[i][x]) * calc
    calc += 1
  
print(sum)
