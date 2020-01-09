import random		
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']	
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList): #This function return a ranadom word from the passed list of words
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):#this is used for the display of the things 
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')#this will print out the missed letters typed
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord) #this will take the secret random genereted word and just fill the words with blanks

    for i in range(len(secretWord)): #this replace the blank correctly with gussed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()
 

def getGuess(alreadyGussed): # this returns the letter the player entered. and the function makes sure the player entered a single letter.
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGussed:
            print('You have already guessed that letter Please choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please type a letter!')
        else:
            return guess

def playAgain(): #this function return true if the player wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N') #this is part of the start of the game checking if the game is done yet
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord) 
    
    guess = getGuess(missedLetters + correctLetters) # lets the player enter a letter

    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True #this checks if the player won
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            
        if foundAllLetters: #this will show if the player won 
            print('Yes! The sercres word is "' + secretWord + '"! You have won!')
            gameIsDone = True
            
    else:
        missedLetters = missedLetters + guess #check if the player has guess to many times and lost.
            
        if len(missedLetters) == len(HANGMAN_PICS) - 1: 
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Im Sorry! u are out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses the word was "' + secretWord + '"')
            gameIsDone = True
            
    if gameIsDone: #this displays if the player types yes 2 play again
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break


            

            

    
