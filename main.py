import random
from replit import clear
import words as HW
import art as HA

chosen_word = random.choice(HW.word_list)
guess_word = ["_" for x in range(len(chosen_word))]
guess = ""
health = 6
isCorrect = False
isRepeated = False

def print_word(word):
  print("Hidden Word: " + " ".join(word))

def printGuess():
    global isCorrect
    global health
    global guess
    
    clear()

    text = ''
    # Print the value of guess_word
    for x in range(len(chosen_word)):
      text += guess_word[x]
    print_word(text)
  
    # Check if guess is not correct then display text and decrease life
    if isCorrect is False:
        print(f"You've guessed {guess}, that's not in the word. You lose a life")
        health -= 1
    if isRepeated is True:
        print(f"You've already guessed {guess}")
    # Print hangman art
    print(HA.stages[health])

def makeGuess():
    global guess
    global isCorrect
    global isRepeated

    isCorrect = False
    isRepeated = False
    guess = input("\nChoose a word: ").lower()
    if guess not in guess_word:
        for x in range(len(chosen_word)):
            if guess == chosen_word[x]:
                guess_word[x] = guess
                isCorrect = True
    else:
        isRepeated = True
        isCorrect = True

    printGuess()


print(HA.logo + "\n")
print_word(guess_word)
while "_" in guess_word and health != 0:
    makeGuess()
if health != 0:
    print(f"Good Job! You guessed the word with {health} health remaining!\n")
else:
    print(f'GAME OVER. The mystery word you failed to guess is \"{chosen_word}.\"\n')


