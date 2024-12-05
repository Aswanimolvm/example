n=10
for i in range(n):
    for j in range(n):
        print(" * ",end="")

    n=n-1
    for k in range(i):
        print(" ",end="")

    print()