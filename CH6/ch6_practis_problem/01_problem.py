a1 = int(input("enter 1st number :"))
a2 = int(input("enter 1st number :"))
a3 = int(input("enter 1st number :"))
a4 = int(input("enter 1st number :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is gretest ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is gretest ",a2)

elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is gretest ", a3)

elif(a3==a2 and a3==a1 and a3==a4):
    print("all numbers are equal")

else:
    print("a4 is gretest ", a4)

    