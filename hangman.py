from class_hangman import Hangman
import random
import game_data
import os


def run(movie):
    game = Hangman(movie)
    game.create_session()
    yn = input("CONTINUE PLAYING?[Y/N]: ")
    if yn == 'y' and 'Y':
        menu()


def menu():
    os.system('clear')
    print("""
    WELCOME TO HANGMAN
    
    PRESS C FOR CUSTOM MOVIE NAME
    PRESS ANY KEY TO START
    
    """)
    op = input("ENTER YOUR CHOICE: ")[0]
    if op != 'c' and 'C':
        movie = random.choice(game_data.movies).upper()
        run(movie)
    else:
        movie = input("Enter movie name: ")
        run(movie.upper())


menu()
