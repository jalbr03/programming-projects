import random

num = random.randint(1,10)
done = True

while(done):
    mynum = int(input("guess a number between 1 and 10 "))

    if(mynum == num):
        print("correct! Now you may be free.")
        done = False
    else:
        tryagin = input("Wrong, would you like to try again? y/n ")
        if(tryagin == "n"):
            done = False
        else:
            pass
