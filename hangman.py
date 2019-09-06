from class_hangman import Hangman
import random
import game_data
import os


def run(movie, n=2):
    game = Hangman(movie)
    game.create_session(n)
    guess = game.get_input()
    game.sort_input(guess)
    yn = input("CONTINUE PLAYING? [Y/N]: ").lower()
    if yn == 'y':
        menu()
    os.system('clear')


def menu():
    os.system('clear')
    print("""
    WELCOME TO HANGMAN
    
    PRESS E FOR ENGLISH MOVIES
    PRESS C FOR CUSTOM MOVIE NAME
    PRESS X FOR EXTRA DIFFICULTY
    PRESS ANY OTHER KEY TO START
    
    """)
    op = input("ENTER YOUR CHOICE: ")[0].lower()
    if op == "c":
        movie = input("Enter movie name: ").upper()
        run(movie)
    elif op == "e":
        movie = random.choice(game_data.english_movies).upper()
        run(movie)
    elif op == "x":
        movie = random.choice(game_data.hindi_movies).upper()
        run(movie, 0)
    else:
        movie = random.choice(game_data.hindi_movies).upper()
        run(movie)


if __name__ == "__main__":
    menu()
