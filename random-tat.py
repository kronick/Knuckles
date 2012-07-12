import random

f = open("4lw.txt", "r")
e = open("8lw.txt", "r")
fours = f.readlines()
eights = e.readlines()

for i in range(0,50):
  if random.random() < 0.75:
    first = random.randrange(0, len(fours))
    second = random.randrange(0, len(fours))

    print fours[first].strip(), fours[second].strip()

  else:
    print eights[random.randrange(0,len(eights))].strip()
