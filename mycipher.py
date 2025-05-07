import sys

shift = 26 - sys.argv
for line in sys.stdin:
  line = line.upper()
  cypher=""
  for c in line:
    if c.isalpha():
      if (c+shift) < 27:
        cypher+=(c+shift)
      else:
        cypher+=(c+shift-26)
  count = 1
  for l in cypher:
    if count%5 == 0:
      if count%50 == 0:
        print(l, end="\n")
      else:
        print(l, end=" ")
    else:
      print(l, end="")
    count+=1