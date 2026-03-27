import random


class Train:
    def __init__(self, trainNo):

        self.trainNo = trainNo
        

    def book(self, fro, to):
        print(f"Ticket is book in train no. {self.trainNo} from {fro} to {to}")

    def getStatus(self ):
        print(f"Train no. {self.trainNo} is running")

    def getFare(self, fro, to):
        print(f"Ticket is book in train no. {self.trainNo} from {fro} to {to} is {random.randint(222, 5555)}")




a = Train(23)
a.book("Rampur", "Delhi")
a.getStatus()
a.getFare("Rampur", "Delhi")




    