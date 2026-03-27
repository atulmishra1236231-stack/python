class Calculator :
    def __init__(self, n):        #creating a consructior
        self.n = n

#create different function according to question

    def square(self):
        print(f"the square is {self.n*self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")


number = int(input("enter a number : "))

a = Calculator(number)
a.square()              # calling square function
a.squareroot()           #calling square root funcion
a.cube()                 #calling cube function