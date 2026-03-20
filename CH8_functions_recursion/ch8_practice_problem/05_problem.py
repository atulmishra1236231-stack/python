'''
****
***
**
*              n = 4



'''
def p(n):
    if(n==0):
        return
    print("*"*n)
    p(n-1)

n = int(input("enter a number : "))
p(n)