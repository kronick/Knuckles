import re

f = open("simpsons-words.txt", 'r')
#f  = open("/Users/kronick/Desktop/unsorted/words", "r")
o = open("4lw.txt", 'w')

pattern = re.compile("[^0-9A-Za-z%]")

total = 0
added = 0
for line in f:
  clean = line[7:22].strip()
  clean = pattern.sub("", clean)
  #clean = line.strip()
  if len(clean) == 4:
    #print line[7:12].strip()
    print clean
    o.write(clean + "\n")
    added += 1

  total += 1

f.close()
o.close()
print added, "/", total
print "Done."
