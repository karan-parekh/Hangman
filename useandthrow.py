
""" MOVE ALONG! NOTHING TO SEE HERE """
import random
m = 'Bhaag Milkha Bhaag'
m = m.upper().replace(' ', '')
print(m)
c = random.choice(m)
print(c)

# hangman = ' [H][A][N][G][M][A][N]'
# h = 7
# for i in range(1, h*3, 1):
#     if hangman[i+1].isalpha():
#         hangman = hangman.replace(hangman[i+1], 'X', 1)
#
# print(hangman)


# for i in range(3):
#     # while hangman[i].isalpha():
#     if not hangman[i].isalpha():
#         hangman = hangman.replace(hangman[i+1], 'X', 1)
#     # else:
#     #     i += 1
