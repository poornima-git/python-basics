import random
name = input("what is ur name:")
print("Hello" " " + name, "lets begin the game" )
words = ["apple","mango", "orange"]
turns = 6
sel_words = random.choice(words)
guesses = []
for i in range(len(sel_words)):
    guesses += "_"
print(guesses)
game_over = False
while not game_over:
    guessed_letter = input("guess a letter:\n").lower()
    for position in range(len(sel_words)):
        i = sel_words[position]
        if i == guessed_letter:
            guesses[position] = guessed_letter
    print(guesses)
if guessed_letter not in sel_words:
    turns -= 1
    if turns == 0:
        game_over = True
    print("you lose")
    if "_" not in guesses:
        game_over = "True"
    print("you win")

   


    