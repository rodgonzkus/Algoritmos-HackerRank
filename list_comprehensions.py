##### List Comprehensions #####
#x=1; y=1; z=2; n=3
combinations_1 = list()
combinations_2 = list()
for a in range(0, x+1):
    for b in range(0,y+1):
        for c in range(0,z+1):
            if a+b+c != n:
                combinations_1.append([a,b,c])
            else:
                combinations_2.append([a,b,c])
print(combinations_1)    