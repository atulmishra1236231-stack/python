def greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        print("n1 is gretest ",n1 )
    elif(n2>n1 and n2>n3):
        print("n2 is gretest ", n2)
    else:
        print("n3 is gretest", n3)
    print("thank you")

n1 = int(input("enter number n1 : "))
n2 = int(input("enter number n2 : "))
n3 = int(input("enter number n3 : "))
print(greatest(n1, n2, n3))