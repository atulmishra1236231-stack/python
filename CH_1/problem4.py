import os

# specify the directory path
path = "D:/BME"

# get list of files and directories
contents = os.listdir(path)

# print each item
print("Contents :")
for item in contents:
    print(item)