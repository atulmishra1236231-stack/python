def rem(l, word):
    for item in l :
        l.remove(word)
        return l

l= ["atul", "avtar", "om", "krishna", "baadmass"]
word = input("give the name you want to remove from the list : ")
print(rem(l, word))