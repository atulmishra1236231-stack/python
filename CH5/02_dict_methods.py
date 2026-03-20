marks = {
    "atul" : 100,
    "rashi" : 90,
    "saloni" : 95
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"atul": 97})
print(marks)
print(marks.get("rashi"))