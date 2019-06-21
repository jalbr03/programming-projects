'''
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

s = "QWERTYUIOPASDFGHJKLZXCVBNM"
ls = list(s)

for i in range(0,26):
    index = ls.index(capitals[1-1])
    print(index)
'''
#ask for a string
string = input("type a sentence ")
#convert the string to a list
ls = list(string)
#get the length of the list
stringlen = len(ls)

#initialize an empty list
NumPlaceList = []

#run the loop for the amount in stringlen
for i in range(0, stringlen):
    #check each letter in the list using i
    if(ls[i].isupper()):
        #if ls[i].isupper() is true add i to NumPlaceList
       NumPlaceList.append(i)

#print the finished list
print(string + " --> " + str(NumPlaceList))