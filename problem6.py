squareSum = 0
sumSquares = 0
for i in range(1,101):
    sumSquares = sumSquares + i*i
    squareSum = squareSum + i
squareSum = squareSum*squareSum
print squareSum - sumSquares 