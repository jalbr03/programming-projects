#vars-
done = False
num = 0
total = 0
numeric = True;

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

while not done:
    total = 0
    num = input("type a number or type quit to end the program ")

    if(is_number(num) == False):
        if(num.capitalize() == "Quit"):
            done = True

    else:
        num = int(num)
        for i in range(0,num+1):
            total += i
        print(total)

