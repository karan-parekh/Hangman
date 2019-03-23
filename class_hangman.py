import os
import random


class Hangman:
    m = h = 0

    def __init__(self, movie):
        self.movie = movie
        self.hangman = ' [H][A][N][G][M][A][N] '
        self.stage = ''

    def update_playground(self):
        # os.system('clear')  # TO BE USED ONLY WHEN RUNNING IN TERMINAL
        print(self.stage)
        print(self.hangman)
        print(self.movie)  # for debugging

    def create_session(self):
        for i in self.movie:
            if i != ' ':
                self.stage = self.stage + '_ '
            else:
                self.stage = self.stage + '  '

        if len(self.movie) < 5:
            pass

        word = self.movie.replace(' ', '')
        clue = random.choice(word)
        self.sort_input(clue)

        self.update_playground()

    def get_input(self):
        guess = input("Enter your guess >>  ").upper()
        if not guess.isalpha() or len(guess) > 1:
            print("Please Enter only one character between A to Z")
            self.get_input()
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
        if '_' in self.stage:
            self.sort_input(self.get_input())
        else:
            print("YOU WON")

    def update_hangman(self, h):
        for i in range(1, h*3, 1):
            if self.hangman[i+1].isalpha():
                self.hangman = self.hangman.replace(self.hangman[i+1], 'X', 1)
        self.update_playground()
        if h != 7:
            self.sort_input(self.get_input())
        else:
            print("YOU LOST")
            print("The movie was: " + self.movie)

    def sort_input(self, guess):
        if guess in self.movie:
            self.m += 1
            self.update_stage(guess)
        else:
            self.h += 1
            self.update_hangman(self.h)
