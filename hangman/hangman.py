# graham hirsch and millie mince
# cs51a
# assignment 4
# 9/27/19
# making hangman
# we implemented all 3 of the extra credit operations

from movies import *
from random import *

movies = get_movies()

def generate_random_movie():
    """generates a random movie from the selection of movies imported"""
    movies = get_movies()
    random_movie = choice(movies)
    return random_movie

def generate_underscore(movie_name):
    """takes the random movie and turns it into dashes instead of letters, 
    hiding it from the user"""
    underscored_list = []
    for character in movie_name:
        if character == " ":
            underscored_list.append(" ")
        else:
            underscored_list.append("-")
    return underscored_list
    
def list_to_string(l_strings):
    """this takes the movie name or guessed letters and returns them as a 
    joined string"""
    delimiter = ""
    stringed = delimiter.join(l_strings)
    return stringed

def capitalize_all(l_strings):
    """capitalizes all letters in a string"""
    res = [] 
    for s in l_strings:
        res.append(s.capitalize())
    return res

def insert_letter(letter, l_strings, movie):
    """inserts a guessed letter into a movie string"""
    underscores = generate_underscore(movie)
    for i in range(len(l_strings)):
        if movie[i] == letter:
        # must use i to indicate a random letter that's guessed
            l_strings[i] = letter
    stringed_guess = list_to_string(l_strings)
    # concatenates the movie string
    capitalized_stringed_guess = capitalize_all(stringed_guess)
    return capitalized_stringed_guess

def play_hangman():
    """play's hangman, combining the last few functions"""
    tup_movie = generate_random_movie()
    movie = tup_movie[0]
    underscored_movie = generate_underscore(movie)
    stringed_movie = list_to_string(underscored_movie)
    guessed_letters = []
    incorrect_guesses = []
    running = True
    print(stringed_movie)
    guesses_taken = 0
    MAX_GUESSES = 10
    while running:
        guesses_taken = guesses_taken + 1
        letter = input("Guess a letter: ")
        if letter in guessed_letters:
            print("\n" + "You've already guessed this! Try again.")
        # (extra credit) doesn't allow for the user to guess the same letter twice because it will not append a repeated guess to the guessed letters list
        elif letter in movie:
            stringed_movie = insert_letter(letter, underscored_movie, movie)
            guessed_letters.append(letter)
            guessed_letters.append(" ")
            print("\n" + "Good Job! Guess a new letter!" )
        # when a correct letter is guessed, the function puts the letter into
        # the movie string
        elif not letter in movie:
            guessed_letters.append(letter)
            guessed_letters.append(" ")
            incorrect_guesses.append(letter)
            print("\n" + "Uh-Oh... Guess a new letter.")
        # when an incorrect letter is guessed, the function puts the letter into
        # the Guessed Letters string
        stringed_guess = list_to_string(stringed_movie)
        print(stringed_guess)
        # variable for inputing correctly guessed letters into the movie name
        capitalized_guessed = capitalize_all(guessed_letters)
        stringed_guessed_letters = list_to_string(capitalized_guessed)
        print("Guessed letters: " + stringed_guessed_letters)
        # variable for inputing incorrectly guessed letters under the movie
        # name
        number_of_incorrect_guesses = len(incorrect_guesses)
        guesses_left = MAX_GUESSES - number_of_incorrect_guesses
        print("Guesses left: " + str(guesses_left))
        if guesses_left == 0: 
            # (extra credit)this if statement limits the number of incorrect guesses a player can have to 10
            print("You've maxed out guesses! Uh-Oh!")
            print("The movie was: " + movie)
            print("Incorrect Guesses: " + list_to_string(capitalize_all(incorrect_guesses)))
            break
        if not "-" in stringed_guess:
            print("\nYou Win!" + "\n" + "The movie was: " + stringed_guess + "\n" + "You guessed it in " + str(guesses_taken) + " guesses")
            print("Incorrect Guesses: " + list_to_string(capitalize_all(incorrect_guesses)))
            # (extra credit) prints the incorrect guesses when the game finishes
            break
        # function for when the user finally guesses the name of the movie
            
        
if __name__ == "__main__":
    """function used to automatically begin playing the game when the code is 
    run"""
    play_hangman()