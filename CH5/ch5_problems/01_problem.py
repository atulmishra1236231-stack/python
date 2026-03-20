d = {
   "namaste": "hello",
    "paani": "water",
    "roti": "bread",
    "dost": "friend",
    "ghar": "house"
}
word = input("enter a word : ")
print("MEANING : ", d.get(word, "word is not present in distionary"))
print("length of dictionary : " , len(d))