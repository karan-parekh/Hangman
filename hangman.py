from class_hangman import Hangman
import random
import game_data


def run(movie=random.choice(game_data.movies).upper()):
    game = Hangman(movie)
    game.create_session()
    guess = game.get_input()
    game.sort_input(guess)


def menu():
    print("""
    WELCOME TO HANGMAN
    
    PRESS C FOR CUSTOM MOVIE NAME
    PRESS ANY KEY TO START
    
    """)
    op = input("ENTER YOUR CHOICE: ")
    if op != 'c' or 'C':
        run()
    else:
        movie = input("Enter movie name: ")
        run(movie.upper())


menu()
