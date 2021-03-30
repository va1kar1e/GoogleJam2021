testcase = int(input())
for t in range(testcase):
  x, y, val = input().split(" ")
  val = val.lower()
  f1, f2 = 0, 0
  prev = val[0]
  for i in range(1, len(val)):
    if val[i] == prev: continue
    if val[i] == "j":
      if prev == "c":
        f1 += 1
      prev = val[i]
    elif val[i] == "c":
      if prev == "j":
        f2 += 1
      prev = val[i]
  print("Case #%d: %d" % (t+1, f1*int(x) + f2*int(y)))
