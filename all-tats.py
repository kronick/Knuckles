import random

f = open("4lw.txt", "r")
o = open("all-simpsons.txt", "w")
fours = f.readlines()
tats = []

for first in range(0,len(fours)):
  for second in range(0, len(fours)):
    tats.append(fours[first].strip() + " " + fours[second].strip())

random.shuffle(tats)
for tat in tats:
  print tat
  o.write(tat + "\n")
