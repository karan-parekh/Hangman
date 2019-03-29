import os
import random


class Hangman:
    h = 0

    def __init__(self, movie):
        self.movie = movie
        self.hangman = ' [H][A][N][G][M][A][N] '
        self.stage = ''
        self.end = False

    def update_playground(self):
        os.system('clear')  # TO BE USED ONLY WHEN RUNNING IN TERMINAL
        print(" " + self.stage)
        print("\n" + self.hangman)

    def give_clues(self, n=1):
        clues = random.sample(self.movie.replace(' ', ''), n)
        if len(set(clues)) < n:
            self.give_clues()
        for clue in clues:
            self.update_stage(clue)

    def create_session(self):
        for i in self.movie:
            self.stage = self.stage + '_ ' if i != ' ' else self.stage + '  '
        self.give_clues()

    def get_input(self):
        guess = input("Enter your guess >>  ").upper()
        if not guess.isalpha() or len(guess) > 1:
            print("Please Enter only one character between A to Z")
            guess = self.get_input()
        return guess

    def update_stage(self, guess):
        ls = list(self.stage)
        lm = list(self.movie)
        for i in range(len(lm)):
            if lm[i] == guess:
                ls[i*2] = lm[i]
        self.stage = ''
        for x in ls:
            self.stage += x
        self.update_playground()
        if '_' not in self.stage:
            print("YOU WON")
            self.end = True

    def update_hangman(self):
        self.h += 1
        for i in range(1, self.h*3, 1):
            if self.hangman[i+1].isalpha():
                self.hangman = self.hangman.replace(self.hangman[i+1], 'X', 1)
        self.update_playground()
        print(" NOPE ")
        if self.h == 7:
            print(" YOU LOST\n The movie was: " + self.movie)
            self.end = True

    def sort_input(self, guess):
        self.update_stage(guess) if guess in self.movie else self.update_hangman()
        if not self.end:
            self.sort_input(self.get_input())
