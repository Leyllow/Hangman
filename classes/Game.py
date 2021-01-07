import re

class Game():
    secret_word = ""
    try_number = 6
    current_word_state = []
    letters_tried = []

    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.current_word_state = ["_"] * len(secret_word)

    def get_current_word_state(self):
        return "".join(self.current_word_state)

    def get_secret_word(self):
        return self.secret_word

    def set_current_word_state(self, letter):
        for index in [m.start() for m in re.finditer(letter, self.secret_word)]:
            self.current_word_state[index] = letter
            
    def get_try_number(self):
        return self.try_number

    def set_try_number(self):
        self.try_number -= 1

    def check_secret_word(self, letter):
        return letter in self.secret_word

    def game_won(self):
        return "".join(self.current_word_state) == self.secret_word

    def set_letters_tried(self, letter):
        self.letters_tried.append(letter)
            
    def check_letters_tried(self, letter):
        return letter in self.letters_tried

    def draw_hangman(self):
        print("-------")
        print("|     |")
        if self.try_number < 6:
            print("|     O")
        else:
            print("|      ")
        if self.try_number < 5:
            if self.try_number == 4:
                print("|     |")
            elif self.try_number == 3:
                print("|     |\\")
            elif self.try_number < 3:
                print("|    /|\\")
        else:
            print("|      ")
        if self.try_number < 2:
            if self.try_number == 1:
                print("|    /")
            elif self.try_number == 0:
                print("|    / \\")
        else:
            print("|      ")
        print("|      ")
        print(self.get_current_word_state())