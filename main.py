import time
import json
import random
import requests
import unidecode
from googletrans import Translator
from classes.Game import Game

# Random word generator
def generated_word():
    response = requests.get(
        "http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    data = response.json()
    word = random.choice(data)
    while not word.isalpha():
        word = random.choice(data)
    return word

# Expecting player input to pick a language
def language_picked():
    language = input(
        "Welcome to the Hangman ! Wich language would you like to use ? \n(use the first two letter of your language, ex: 'fr' for French\n")
    while len(language) != 2 or not language.isalpha():
        language = input("Use only two letters, ex: 'it' for Italian\n")
    print("You chose " + language.upper())
    return language

# Translate the random word generated based on language picked by the player
def translated_word():
    trans = Translator()
    return unidecode.unidecode(trans.translate(generated_word(), src='en', dest=language_picked()).text).lower()

# Game initialization
game = Game(translated_word())

# Write a welcome message
def welcome():
    print("Let's see if you will be able to save the man from hanging ... ;)")

# Check if the player have used all his chances or if he won
def is_game_over():
    return game.get_try_number() == 0 or game.game_won()

# Check if the letter has already been used
#   yes: send a message to warn the player that he already used that letter
#   no: add it to a list of letter been used
# Then check if the letter is in the secret word
#   yes: change current secret word state
#   no: the player lose one chance
def check_word(letter):
    if game.check_letters_tried(letter):
        print("You already tried that one, try another one !")
    else:
        game.set_letters_tried(letter)
        if game.check_secret_word(letter):
            game.set_current_word_state(letter)
            print("Yeah, you found one ! You have %s try left" %
                  game.get_try_number())
        else:
            game.set_try_number()
            print("Nope, no %s in that word ! You have %s try left" %
                  (letter, game.get_try_number()))

# Return the letter chosed by the player, check also if it is only one letter and also not a number
def player_input():
    player_input = input()

    while len(player_input) > 1 or not player_input.isalpha():
        player_input = input("Please type only one letter\n")

    return player_input

# The game !
def start_game():
    welcome()

    while not is_game_over():
        game.draw_hangman()
        check_word(player_input())

    if game.game_won():
        game.draw_hangman()
        print('Bravo ! The word was %s !' % game.get_current_word_state())
    else:
        game.draw_hangman()
        print('You lose :( The word was %s !' % game.get_secret_word())


start_game()
