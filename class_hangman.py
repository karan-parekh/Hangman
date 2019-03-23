import os


class Hangman:
    m = h = 0

    def __init__(self, movie):
        self.movie = movie
        self.hangman = 'HANGMAN'  # '[H][A][N][G][M][A][N]'
        self.stage = ''

    def update_playground(self):
        os.system('clear')  # TO BE USED ONLY WHEN RUNNING IN TERMINAL
        print(self.stage)
        print(self.hangman)
        # print(self.movie)  # for debugging

    def create_session(self):
        for i in self.movie:
            if i != ' ':
                self.stage = self.stage + '_'
            else:
                self.stage = self.stage + 's'

        self.update_playground()

    def get_input(self):
        guess = input("Enter your guess >>  ").upper()
        if not guess.isalpha() or len(guess) > 1:
            print("Please Enter only one character between A to Z")
            self.get_input()
        return guess

    def update_stage(self, guess, m):
        ls = list(self.stage)
        lm = list(self.movie)

        for i in range(len(lm)):
            if lm[i] == guess:
                ls[i] = lm[i]

        self.stage = ''
        for x in ls:
            self.stage += x

        self.update_playground()
        if '_' in self.stage:
            self.sort_input(self.get_input())
        else:
            print("YOU WON")

    def update_hangman(self, h):
        print("hangman updated")
        for i in range(h):
            self.hangman = self.hangman.replace(self.hangman[i], 'X', 1)
        self.update_playground()
        if h != 7:
            self.sort_input(self.get_input())
        else:
            print("YOU LOST")

    def sort_input(self, guess):
        if guess in self.movie:
            self.m += 1
            self.update_stage(guess, self.m)
        else:
            self.h += 1
            self.update_hangman(self.h)
