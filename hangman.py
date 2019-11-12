#Imports
from __future__ import print_function
import random
import os

#Defining a function to clear the terminal window, Only works in CMD!
def clear():
    os.system('cls')

class Hangman_Class:
    def __init__(self):
        #Dictionary with Empty values which progressivly will be set when the guess is wrong.
        self.bodyparts = {'head': '', 'leftarm': '', 'rightarm': '', 'body': '', 'body2': '', 'leftleg': '', 'rightleg': ''}
        #This is the list of available words to guess on, it choses randomly which word.
        wordlist = ['APPLE', 'TRUCK', 'SCHOOL', 'ORANGE', 'KITCHEN']
        self.word = wordlist[random.randint(0, 4)]
        self.currentfailguess = 0
        self.currentsuccessguess = 0
        self.maxguesses = 7
        #Attribute to show the underscores for shadowing the hidden word.
        self.maskedword = [' _ ' for word in range(0, len(self.word))]


    def ASCI_hangman(self):
        clear()
        #Adds a body part to the bodyparts dictionary for every failed guess.
        if self.currentfailguess == 1:
            self.bodyparts['head'] = 'O'
        elif self.currentfailguess == 2:
            self.bodyparts['leftarm'] = '\\'
        elif self.currentfailguess == 3:
            self.bodyparts['body'] = '|'
        elif self.currentfailguess == 4:
            self.bodyparts['rightarm'] = '/'
        elif self.currentfailguess == 5:
            self.bodyparts['body2'] = '|'
        elif self.currentfailguess == 6:
            self.bodyparts['leftleg'] = '/'
        elif self.currentfailguess == 7:
            self.bodyparts['rightleg'] = '\\'

        #Prints the ASCI-Art
        print(
            """
This is Hangman, Save him!
_________
| /     |
|/      {head}
|     {larm} {body} {rarm}
|       {body2}
|      {lleg} {rleg}
        """
                .format(head=self.bodyparts['head'], larm=self.bodyparts['leftarm'], body=self.bodyparts['body'],
                        body2=self.bodyparts['body2'], rarm=self.bodyparts['rightarm'], lleg=self.bodyparts['leftleg'],
                        rleg=self.bodyparts['rightleg'])
        )
    #Function to engage a new game.
    def start_game(self):
        print(""" Let's play a game, guess the word or the man will be hanged!""")
        self.ASCI_hangman()
        #Checking that you are not out of guesses.
        while self.currentfailguess < self.maxguesses:

            guess = input('What is your guess?').upper()
            try:
                #Confirms that you only typed one letter.
                if len(guess) < 1 or len(guess) > 1:
                    raise ValueError
                #Variable to find the index of the letter you guessed.
                guessed = self.word.find(guess)
                #Makes sure you dont waste your guess by guessing the same letter twice.
                if guess in self.maskedword:
                    print('You have already guessed this letter, Try again!')
                #If your guess are successfull it will replace the underscore with your guess.
                elif guessed != -1:
                    counter = -1
                    self.currentsuccessguess += 1
                    for letter in self.word:
                        counter += 1
                        if letter == guess:
                            self.maskedword[counter] = guess

                    self.ASCI_hangman()

                    print(*self.maskedword, sep='')
                    #Checks if you are done with all the letters
                    if ' _ ' not in self.maskedword:
                        print('Congratulations you have successfully saved the poor man!')
                        exit()
                    print('You got it!')
                #If you guessed wrong letter it will count up and add a bodypart to the ASCI-Art.
                elif guessed == -1:
                    self.currentfailguess += 1
                    self.ASCI_hangman()
                    print(*self.maskedword, sep='')
                    print('Your letter {} was not in the word, try again'.format(guess))


            #If you typed more than two characters this will be risen
            except ValueError:
                print('You can only pick one character')

        #If you failed to save the man in 7 tries, the game will end.
        self.ASCI_hangman()
        print(*self.maskedword, sep='')
        print('You have failed your mission, the man is hanged!')


game = Hangman_Class()
game.start_game()
