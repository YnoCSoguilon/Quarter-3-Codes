names = ["Me", "Lia", "Jake"]

steps = [
  
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
  
]

print(f"{'Name':<6} |  day 1:  |  day 2:  |  day 3:  |  day 4:  |  day 5: ")

for stuff, hey in zip(names, steps):
  print(f"{stuff:<6} | {hey[0]:<8} | {hey[1]:<8} | {hey[2]:<8} | {hey[3]:<8} | {hey[4]:<8}")

highest = 0
highestperson = ""
array = []

for y in range(len(names)):
  summ = 0
  summ = sum(steps[y])
  array.append(summ)
  print(f"Total of {names[y]} is: {array}")
  if 0 = 0:
    highestperson = names[y]
mean = max(array) - min(array)
print(f"And the person with the highest amoubt of steps is... {highestperson}!")
print(f"The mean is... {mean}!")

