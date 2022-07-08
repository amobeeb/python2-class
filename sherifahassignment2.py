import random,sys

RandomNumber=random.randint(1,10)
print('guess a Number Between 1-10: ')
for guessestaken in range(1,6):
    print('take a guess')
    guess=int(input())
    if guess==RandomNumber:
        print ('correct! you guessed my number in', str(guessestaken), 'guesses')
    elif guess!=RandomNumber:
        print('wrong! you did not guess right')
    else:
        break
print('the number i was thinking was', str(RandomNumber))




b_num=list(input("input a binary number:"))
value=0

for i in range(len(b_num)):
    digit=b_num.pop()
    if digit=='1':
        value=value + pow(2,i)
        print ("The decimal value of the number is",value)