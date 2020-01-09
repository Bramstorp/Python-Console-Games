#this is the random number generator
import random

guessesTaken = 0

print('Hello! What is ur name?')
myName = input() #this makes a var of the name input

number = random.randint(1, 20) #this is used as a random number generator between 1 and 20
print('well, ' + myName + ' I am thinking of a number between 1 and 20.')

while guessesTaken < 6: #this is used if the used has taken less than 6 tryes.
    print('Take a guess. ')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1 #this just add 1 to the guess value when a guess has been taken.

    if guess < number:
        print('Your guess i too low')
    
    if guess > number:
        print('Your guess is to high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job,' + myName + '! You gussed my number in ' + guessesTaken + ' guesses!')
    guess = input()

if guess != number:
    number = str(number)
    print('Nope. The number i was thinking of was ' + number)
    guess = input()