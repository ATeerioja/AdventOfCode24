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
    print(f"{i} / {len(data)}")
    if i % 2 == 0:

      for z in range(memory[calc][1]):
        tempLine.append(str(memory[calc][0]))

      calc += 1

    else:
      for z in range(int(data[i])):
        tempLine.append(".")

    line.append(tempLine)

print(line)

for rev in reversed(range(len(line))):
  try:
    print(line[rev][0])
    if(line[rev][0] != "."):
      spaceReq = len(line[rev])

      for i in range(len(line)):
        print(line[i].count("."))
        if(line[i].count(".") >= spaceReq):
          for x in range(len(line[rev])):
            if(line[rev][x] != "."):
              line[i][x] = line[rev][i]
              line[rev][i] = "."

  except:
    print("Empty")
    continue

print(line)

"""
  for x in range(len(line)):
    print(f"{x} / {len(line)}")
    if(line[x] == "."):

      for reverse in reversed(range((len(line)))):
        if( line[reverse] != "."):
          value = line[reverse]
          line[reverse] = line[x]
          line[x] = value
          break

  sum = 0
  for num in range(len(line)):
    print(f"{num} / {len(line)}")
    if line[num] == ".":
      continue

    sum += num * int(line[num])
  
  print(sum)
"""