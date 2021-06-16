a = [1,2,3,4,5,6]
even=odd=0
for i in a:
    if i%2 == 0:
        even=even+i
    else:
        odd=odd+i
    print(even)
    print(odd)

