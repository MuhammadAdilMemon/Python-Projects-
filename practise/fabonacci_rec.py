#fabonacci by recursion
def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabo(n-1)+fabo(n-2)

def printfab(n):
    for i in range(0,n+1):
        print(str(fabo(i)) + " " , end="")


printfab(6)