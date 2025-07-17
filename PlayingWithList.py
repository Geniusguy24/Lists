L = [4,5,1,2,9,7,10,8]

print("Original List: ", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum = ", count)
print("average = ", avg) 

L.sort()

print("Smallest Element: ", L[0])
print("Biggest Element: ", L[-1])

print("Ascending order: ", L)