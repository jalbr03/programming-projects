#ask for numbers-------------------------------------
WhatIsTheItem =  input("What is the items cost ")  #|
try:                                               #|
    #converting "WhatIsTheItem" into a float       #|
    WhatIsTheItem = float(WhatIsTheItem)           #|
except ValueError:                                 #|
    print("Error: Fill in the lines with numbers.")#|
    exit()                                         #|
quarters = input("how many quarters do you have ") #|
dimes = input("how many dimes do you have ")       #|
nickels = input("how many nickels do you have ")   #|
pennies = input("how many pennies do you have ")   #|
#----------------------------------------------------

#declar output
output = []

#turn all of the vars in to a list
totalchange = [int(quarters), int(dimes), int(nickels), int(pennies)]


#if the user put all of the numbers in correctly code and the code will run
def change_enough(change, item):
    totalmoney = 0

    # check if the user put all of the numbers in properly
    try:
        change = [totalchange[0]*0.25, totalchange[1]*0.10, totalchange[2]*0.05, totalchange[3]*0.01,]
    # except the Error and quit
    except ValueError:
        print("Error: Fill in all of the lines with numbers.")
        exit()

    for i in range(0,4):
        #add all of the numbers in the list to the variable totalmoney
        totalmoney += change[i]
    #round totalmoney to the second decimal place
    totalmoney = round(totalmoney, 2)

    #adding the numbers to a list named output
    output.append(totalmoney)
    output.append(item)
    #return True or False
    if(totalmoney >= item):
        return True
    else:
        return False

#print true or false
print(change_enough(totalchange, WhatIsTheItem))

#tell the user how much they are over
if(change_enough(totalchange, WhatIsTheItem) == True):
    print("you are over by $" + str(round(float(output[0] - output[1]),2)))

#tell the user how much they are under
if(change_enough(totalchange, WhatIsTheItem) == False):
    print("you need $" + str(round(float(output[1] - output[0]),2)))
