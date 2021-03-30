def checkProbRev(n, cost):
  if cost < n - 1: return []
  val = []
  costTemp, b = 0, 1
  for i in range(n - 1, 0, -1):
    b += 1
    if costTemp + i + b - 1 >= cost:
      val += [cost - (costTemp + i - 1)] + [1 for i in range(i - 1)]
      costTemp = cost
      break
    val.append(b)
    costTemp += b
  if costTemp < cost: return []
  return val

testcase = int(input())
for t in range(testcase):
  n, c = [int(i) for i in input("").split(" ")]
  revOccur = checkProbRev(n, c)
  if revOccur != []:
    val = [int(i) for i in range(1, n + 1)]
    for i in range(len(revOccur)):
      start = (len(val) - 1) - (i + 1)
      val = val[:start] + val[start: (start + revOccur[i])][::-1] + val[(start + revOccur[i]):]
    print("Case #" + str(t + 1) + ": " + (" ").join([str(i) for i in val]))
  else:
    print("Case #" + str(t + 1) + ": " + "IMPOSSIBLE")
