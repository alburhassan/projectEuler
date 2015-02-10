i =20
multiple = 1
for x in range (2,i+1):
    multiple = multiple*x
print multiple
for y in range (2,i+1):
    if multiple/y%y == 0:
        multiple = multiple/y
print multiple