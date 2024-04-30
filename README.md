## Hangman 😵🔪
Hangman is a guessing game where a hidden word, phrase, or sentence is provided and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.

# Instructions

The objective is to guess the word before the hanging man is completed. The user will be given a random word and needs to guess it, one letter at a time.

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Hidden Word: _ _ _ _ _ _
Choose a word: 
```

If the user's guess exists in the hidden word, it will fill out the blanks and continue to ask the player for another guess.
```
Hidden Word: _ a _ _ _ _ a

  +---+
  |   |
      |
      |
      |
      |
=========

Choose a word:
```

If the user fails to guess the hidden word, the hangman will appear, and a game-over notification will be displayed. Otherwise, a winner notification will be displayed.
```
Hidden Word: n a p _ _ _ a
You've guessed r, that's not in the word. You lose a life

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

GAME OVER. The mystery word you failed to guess is "naphtha."

```
```
Hidden Word: n a p h t h a

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Good Job! You guessed the word with 2 health remaining!
```
