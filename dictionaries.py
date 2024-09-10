''''
details = ["sened",11,"red","football",5.5,52]

print( details ) #Prints everything
print (details[2])#prints vaule on 2nd line
print( len(details) )

for i in range( len(details) ):
    print("Value at index {} is {}".format(i,details[i]))

for i in details:
    print("value is {}".format(i))

'''

details = {
"name": "sened",
"age" :"11",
"faviroute-color": "blue",
 "height": 5.5,
 "weight" : 52
 }


print (details)
print (details ["name"])


for i in details:
    print(i)
    print (details[i])

print(details.keys())
print(details.values())

details["name"]="divya"
print(details)

details["blood-group"] = "A=ve"
print(details)

del details["name"]


if "faviroute_food" in details:
    print("yes")