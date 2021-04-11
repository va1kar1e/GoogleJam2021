testcase = int(input())
for t in range(0, testcase):
    n, countadd = int(input()), 0
    numlist = [num for num in input().split(" ")]
    for i in range(0, len(numlist)-1):
      while int(numlist[i]) >= int(numlist[i+1]):
        if len(numlist[i]) >= len(numlist[i+1]):
          numlist[i+1] += "0"
          countadd += 1
        numlist[i+1] = str(int(numlist[i+1]) + 1)
    print("Case #%d: %d" % (t+1, countadd))
