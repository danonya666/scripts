def getRoots(aNeigh):
    def findRoot(aNode, aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode, aRoot[aNode][1])

    myRoot = {}
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode, 0)
    for myI in aNeigh:
        for myJ in aNeigh[myI]:
            (myRoot_myI, myDepthMyI) = findRoot(myI, myRoot)
            (myRoot_myJ, myDepthMyJ) = findRoot(myJ, myRoot)
            if myRoot_myI != myRoot_myJ:
                myMin = myRoot_myI
                myMax = myRoot_myJ
                if myDepthMyI > myDepthMyJ:
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax, max(myRoot[myMin][1] + 1, myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0], -1)
    myToRet = {}
    for myI in aNeigh:
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh:
        myToRet[findRoot(myI, myRoot)[0]].append(myI)
    return myToRet


n = int(input())
m = int(input())
if m == 0:
    print(0)
else:
    d = {}
    inp = []
    for i in range(n):
        d[i] = []

    for i in range(m):
        p = [int(x) for x in input().split(' ')]
        d[p[0]].append(p[1])

    roots = getRoots(d)

    lens = []

    for m in roots.keys():
        lens.append(len(roots[m]))

    lens.sort(reverse=True)
    k = int(input())

    res = 0
    for i in range(k):
        if len(lens) < 1:
            res = 1
            break
        p = [int(x) for x in input().split(' ')]
        for j in range(p[1]):
            while p[0] > 0:
                if p[0] in lens:
                    lens.remove(p[0])
                else:
                    p[0] -= 1

    if len(lens) == 0:
        res = 1

    print(res)
