class Calculator :
    def __init__(self, n):
        self.n = n


    def square(self):
        print(f"the square is {self.n*self.n}")
    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

a = Calculator(45)
a.square()
a.squareroot()
a.cube()