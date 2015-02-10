no = 600851475143
count = 2
while no >count**2:
     while no % count == 0:
         no = no / count
     count = count + 1
print (no)