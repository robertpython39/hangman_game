import random

print("Welcome to hangman! Let's play!")
word_list = ["slap","toys","aware","toy","clear","defeated","bedroom","sophisticated","giant","vague","shoes","intelligent","camera","offend","earthy","beginner",
             "rod","broken","scold","sky","sparkle","loutish","dreary","float","back","peace","mice","selfish","grieving","natural","color","periodic","melt","eager","disarm","branch","strong","welcome",
             "year","stage","letter","notice","comparison","rampant","bone"]
chosen_word = random.choice(word_list)
lives = 6
display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ")
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    else:
        if guess not in chosen_word:
            lives = lives - 1
            print(f"You have left {lives} lives. Try again")
            if lives == 0:
                end_of_game = True
                print(f"The chosen word was {chosen_word}")
                print("You lose!")



