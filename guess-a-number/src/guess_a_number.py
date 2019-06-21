import random

num = random.randint(1,10)
done = False

while not done:
    mynum = int(input("guess a number between 1 and 10 "))

    if(mynum == num):
        print("correct! Now you may be free.")
        done = True
    else:
        if(mynum < num):
            tryagin = input("Wrong to Low, would you like to try again? y/n ")
        if (mynum > num):
            tryagin = input("Wrong to High, would you like to try again? y/n ")
        if(tryagin == "n"):
            done = True
        else:
            pass
