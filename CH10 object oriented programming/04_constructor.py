class Employee():
    language = "pyhon"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method to in which function called automatically
        print("hello how are you")
        self.name = name
        self.salary = salary
        self.language = language

atul = Employee("Atul mishra", 400000, "javascript")
print(atul.name, atul.language, atul.salary)
