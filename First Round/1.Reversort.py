testcase = int(input())
for t in range(testcase):
  element = int(input())
  val = [int(i) for i in input().split(" ")]
  cost = 0
  for i in range(0, len(val)-1):
      minVal = len(val)
      index = 0
      for j in range(i, len(val)):
        if val[j] < minVal:
          minVal = val[j]
          index = j
      temp = val[i:index+1]
      val = val[:i] + temp[::-1] + val[index+1:]
      cost += (index - i) + 1
  print("Case #%d: %d" % (t+1, cost))
