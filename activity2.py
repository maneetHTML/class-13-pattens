n= int(input("number of rows : "))
x=1
for i in range (n):
    for j in range (i+1):
        print (x ,end=" ")
        x=x+1
    print()