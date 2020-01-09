SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS) #this set a length of 52 that lets it know it should allways be between 1-52

def getMode(): #this is used for chooseing to decrypt or enctrypt
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower() #this saves the user input in the mode var
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #this just check for if the user has typed right
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #this will show if the wrong word was typed

def getMessage(): #this is used for saving the user input
    print('Enter your message:')
    return input()

def getKey():# this is used to generated the key
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #this shows the max key size that it can handle 
        key = int(input()) #this saves the input with the int datatype 
        if (key >= 1 and key <= MAX_KEY_SIZE): #this just check if the key number is within the key range
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd': #this is if the has typed d aka decrypt fucntion 
        key = -key #this takes the key function and just take it down one for decrypt
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        
        if symbolIndex == -1:
            translated += symbol
        
        else:
            symbolIndex += key
            
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)           
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode() #these just set so they can be used as global variables
message = getMessage()
key = getKey()
print('You translated text is:')
print(getTranslatedMessage(mode, message, key))