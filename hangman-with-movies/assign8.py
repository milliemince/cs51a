#millie mince
#cs51a
#november 7 2019
#assignment8

#implemented the guessed letters extra credit, I have a comment that shows where this happens. 

from movies import *
import random

class LabeledExample: 
    
    def __init__(self, some_string, some_bool):
        """constructor for class LabeledExample"""
        self.string = some_string
        self.boolean = some_bool
        
    def is_positive(self):
        """returns a boolean of True when the input string is positive,
        False otherwise"""
        return self.boolean
    
    def lowercase(self):
        """makes string lowercase"""
        self.string = self.string.lower()
        
    def get_words(self):
        """returns a list of individual words in self.string"""
        new_l = []
        split_line = self.string.split()
        for word in split_line:
            new_l.append(word)
        return new_l
    
    def contains_word(self, word):
        """"checks if an input word is in self.string, returns True if so,
        False otherwise"""
        return word in self.string
    
    def __str__(self):
        """returns string of the string and whether that string is positive or
        negative"""
        if self.boolean:
            return self.string + "\t" + "positive"
        else:
            return self.string + "\t" + "negative"   
    
class Hangman:
    
    def __init__(self, title):
        """constructer for class Hangman, defining instance variables movie,
        guessed, and current"""
        self.movie = title
        self.guessed = []
        self.current = self.underscore()
    
    def list_to_string(self, somelist):
        """takes a list and returns a string of that list's elements"""
        #E.C.:function that makes guessed letters a string of the letters rather than list
        stringed = ""
        for element in somelist:
            stringed += element
        return stringed
    
    def underscore(self):
        """returns the characters in self.movie as dashes for letters and spaces
        for spaces. this serves as the original state of the game"""
        underscored_list = []
        for character in self.movie:
            if character == " ":
                underscored_list.append(" ")
            else:
                underscored_list.append("-") 
        return underscored_list
    
    def current_state_to_string(self):
        """takes the current list of underscores, guessed letters, and spaces
        and returns a string of these to display to the user the current state
        of the game as a string"""
        stringed = ""
        for element in self.current:
            stringed += element 
        return stringed
    
    def insert_letter(self, someletter):
        """given an input letter, replaces the underscore in self.current
        with the correct letter"""
        for i in range(len(self.movie)):
            if self.movie[i] == someletter:
                self.current[i] = someletter
    
    def guess(self, someletter):
        """given an input letter, inserts the letter where it should be if the 
        letter is in the movie, and appends the letter to the list of guessed
        letters. if the letter is not in the movie, it appends the letter to
        guessed letters but doesn't alter the current state of the game"""
        if someletter in self.movie:
            self.insert_letter(someletter)
            self.guessed.appent(someletter)
        else:
            self.guessed.append(someletter)
            
    def has_won(self):
        """returns True if the entire movie has been guessed, False otherwise"""
        if self.current_state_to_string() == self.movie:
            return True
        else:
            return False
                
    def __str__(self):
        """returns a string consisting of the guessed letters and the current
        state of the game"""
        return "\n___________________\n" + \
               "Guessed letters: " + \
               str(self.list_to_string(self.guessed)) + "\n" + \
               "Movie: " + self.current_state_to_string()       
    
def play_hangman():
    """
    Play the hangman game.    
    """    
    # pick a movie for this game
    (movie, description, year) = random.choice(get_movies())
    print("This is the movie: " + str(movie))

    hangman = Hangman(movie)

    print("*** Movie Hangman ***")
    print("Year: " + str(year))
    print(description)

    # keep playing until they've won
    while not hangman.has_won():
        # print out the state of the game
        print(hangman)

        letter = input("Guess a letter: ")
        letter = letter.lower()
        
        # update the state of the game based on the letter
        hangman.guess(letter)
        
    
    print("___________________")
    print("You win!")
    print("The movie was: " + movie)