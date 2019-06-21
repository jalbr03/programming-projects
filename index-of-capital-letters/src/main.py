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