from time import sleep

def EvenOrOdd(num):
    if num % 2 == 0:
        return "e"
    if num % 2 != 0:
        return "o"

num = float(input("Enter the starting number! > "))
startNum = num
sleepTime = int(input("How long should this wait between each number? > "))
steps = 0
while True:
    if EvenOrOdd(num) == "e":
        num = num / 2
        steps += 1
        sleep(sleepTime)
        print(num)
    elif EvenOrOdd(num) == "o":
        num = num * 3
        num +=1
        steps +=1
        sleep(sleepTime)
        print(num)
    if num == 1:
        print(str(startNum) + " got to 1 in " + str(steps) +" steps!")
        break
input()