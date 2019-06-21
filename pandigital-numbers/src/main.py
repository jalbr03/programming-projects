number = input("type a number ")

def numcheck(numlis):
    numlis = list(number)
    numlis.sort()
    finallist = []
    list2check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for j in range(0,len(numlis)):
        for i in range(0,10):
            if(int(numlis[j]) == i):
                if(i not in finallist):
                    finallist.append(i)
    if(finallist == list2check):
        return True
    else:
        return False

try:
    print(numcheck(number))
except ValueError:
    print("type numbers only")
