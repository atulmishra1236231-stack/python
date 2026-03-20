a = "atul want freedom and\nwant to escape " #"\n" is an escape sequence character
b = "atul want \"freedom\" and want to escape " #\" ...\" is an escape sequence character
c = "atul want freedom and\twant to escape "#"\t" is an escape sequence character
print("hell\\world")  #"\\" is an escape sequence character
print(a)                                   
print(b)
print (c)
print("hello\bworld")  #"\b" is an escape sequence character output is hellworld 
print("Hello\rWorld")  #"\r" is an escape sequence character output is world 
print("Hello\fWorld")  #"\f" is an escape sequence character output is Hello♀World
print("Hello\vWorld")  #"\v" is an escape sequence character output is Hello♂World