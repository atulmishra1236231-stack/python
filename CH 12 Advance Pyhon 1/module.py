def MyFunc():
    print("hello world")

MyFunc()
print(__name__)

if __name__ == "__main__":
    print("we are runing this function directly through main")
else:
    print("you are rinning this function through module")
