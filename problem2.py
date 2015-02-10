prevTerm= 1
currTerm= 2
nextTerm = 0
sumeven= 0
while currTerm< 4000001:
    nextTerm = prevTerm + currTerm
    if currTerm%2 == 0:
        sumeven =  sumeven + currTerm
    prevTerm = currTerm
    currTerm = nextTerm
print sumeven