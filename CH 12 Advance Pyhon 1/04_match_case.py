def student(status):
    match status:
        case 500:
            return "exelent student"
        case 400:
            return "good student"
        case 300:
            return "average student"
        case 200:
            return "fail"
        case _:
            return    "unknown status"

status = int(input("Hey! Write total marks of student in 500, 400, 300 and 200: "))
print(student(status))