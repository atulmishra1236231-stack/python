class Employee:

    language = "python" #class attribute
    salary = 10000000


atul = Employee()
atul.name = "Atul Mishra"  # object attribute
print(atul.name, atul.language, atul.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.language, rohan.salary)

#Here name is object attribute and salar and language are class attribute as they directly
#belong to the  class