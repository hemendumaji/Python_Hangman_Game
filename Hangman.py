import random

stages = ['''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ["ardvark","baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f'Passst, the solution is {chosen_word}')


display = []
for _ in range(word_length):
    display += '_'

end_of_game = False


while not end_of_game:
 guess = input("Guess a letter : ").lower()
#check guessed letter
 for position in range(word_length):
    letter = chosen_word[position]
    # print(f"current position: {position}\n"
    #       f"Current letter: {letter}\n"
    #       f"Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You loose")

        print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

print(stages[lives])