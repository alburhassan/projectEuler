count1 = 1000/3
count2 =1000/5
sum1 = 0
sum2 =0
for i in range(1,count1+1):
    sum1 = sum1 + i*3
for i in range(1,count2):
    if i%3 != 0:
        sum2 = sum2 + i*5
sum = sum1 + sum2
print sum