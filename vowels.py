text = input("Enter the text you want to caclulate ocurrences of vowels for:")

vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
text=text.lower()
print(text)


for i in text:
    if i in vowels:
        vowels[i]=vowels[i]+1

 
print(vowels)