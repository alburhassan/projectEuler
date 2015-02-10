count1 = 999
count2 = 999
palindrome = 0
while count1 >800:
    while count2 >800:
        no = count1*count2
        part1  = no//1000
        part2 = no %1000
        part2 = (no%10)*100 + (no%100 - no%10) + (no%1000 - no%100)/100
        if part1 == part2:
            if no > palindrome:
                palindrome = no
        count2 = count2 -1
    count2 = 999
    count1 = count1 -1
print palindrome