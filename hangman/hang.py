import random
name = input ("what is ur name:\n")
print("Hello" " " + name ,"let's begin")
word = ["computer ", "mobile", "laptop"]
choose = random.choice(word)
print("guess the characters")
guesses = " "
turns = 5
while turns > 0:
    failed = 0
    for char in choose:
        if char in guesses:
            print(char, end =" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("you won")
        print("the word is :", choose)
        break
    print()
    guess = input("guess a letter")
    guesses += guess
    if guess not in choose:
        turns -= 1
        print("wrong")
        print("you have", + turns, "more guesses")
        if turns == 0:
            print("you lose")