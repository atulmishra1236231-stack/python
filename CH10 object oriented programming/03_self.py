class Employee():
    language = "pyhon"
    salary = 1200000
    def getInfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("hello good morning")

atul = Employee()
atul.language = "javaScript"
# print(atul.language, atul.salary)
atul.getInfo()
atul.greet()