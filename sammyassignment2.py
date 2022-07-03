import random, sys

RandComputer=random.randint(1,10)
print('Think of a number between 1 - 10')
for guessestaken in range(1,5):
    print('take a guess')
    userInput=int(input())
    if userInput==RandComputer:
        print('wonderful!, you did well')
        print('you guessed my number in ' + str(guessestaken) + ' guesses')
    elif userInput!=RandComputer:
        print ('eew!, you can do better .')
    else:
        break
print('The Number I was Thinking was '+ str(RandComputer))