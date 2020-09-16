def minOps(n):
    count=0
    while n> 0 :
        if n%2==0:
            temp=n/2
            count+=1
            n=temp
        else:
            temp=n-1
            count+=1
            n=temp
    return count

n=int(input("enter a number: "))
ms=minOps(n)
print("minimum number of operations {} is require to reach {} ".format(ms,n))