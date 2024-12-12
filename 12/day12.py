with open("12/input.txt", "r") as file:
  
  farmLand = [list(x) for x in file.read().split("\n")]

def checkNeighbour(plot, previousPlot):
  global sum
  global area
  globalFarmLands.add(plot)
  if plot in localFarmLands:
    return ((plot[0], plot[1], plot[2]))

  localFarmLands.add(plot)

  neighbours = (set())
  
  if not plot[0] - 1 < 0:
    up = farmLand[plot[0] - 1][plot[1]]
    neighbours.add((plot[0] - 1, plot[1], up))

  if not plot[1] - 1 < 0:
    left = farmLand[plot[0]][plot[1] - 1]
    neighbours.add((plot[0], plot[1] - 1, left))


  if not plot[0] + 1 >= len(farmLand):
    down = farmLand[plot[0] + 1][plot[1]]
    neighbours.add((plot[0] + 1, plot[1], down))

  if not plot[1] + 1 >= len(farmLand[plot[0]]):
    right = farmLand[plot[0]][plot[1] + 1]
    neighbours.add((plot[0], plot[1] + 1, right))

  for neighbour in neighbours:
    if neighbour[2] == plot[2]:
      sum += 1 

    if neighbour[0] == previousPlot[0] and neighbour[1] == previousPlot[1]:
      continue

    elif neighbour[2] == plot[2]:
      checkNeighbour(neighbour, plot)

  area += 1  
  return ((plot[0], plot[1], plot[2]))


  
globalFarmLands = (set())

isoSumma = 0

for row in range(len(farmLand)):
    for index in range(len(farmLand[row])):
      plot = ((row, index, farmLand[row][index]))

      if plot not in globalFarmLands:
        localFarmLands = (set())
        
        print(f"try this {plot}")
        area = 0
        sum = 0
        print(checkNeighbour(plot, plot))
        border = area * 4 - sum
        print(border)
        isoSumma += border * area

print(isoSumma)

