<h1 align="center"> Hangman Game 🤖 🎮 </h1>

![Screenshot from 2023-03-28 22-56-44](https://user-images.githubusercontent.com/77020164/228320042-7b54532c-3a50-461d-ad5b-f35df7e33c4a.png) | ![Screencast from 28-03-23 11_04_52 PM IST](https://user-images.githubusercontent.com/77020164/228322019-d1e6fa01-4270-4d43-b22c-7e99528a25ed.gif)
|-|-|

## Demo Video

[Screencast from 07-04-23 10:04:18 PM IST.webm](https://user-images.githubusercontent.com/77020164/230644778-dfed4349-379e-4b0a-a166-d88325894573.webm)

## Requirements
* Python 3.x
* Tkinter library (which is usually included with Python)


## Getting Started
1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the cloned repository.
3. Run the following command to start the program: `python game.py`

## Blog

Check out our project blog post for more information on the development process and our thoughts on the Hangman Game project:

* [Hangman Game Using Python](https://www.codingninjas.com/codestudio/library/hangman-game-in-python?utm_source=github&utm_medium=organic&utm_campaign=blog-hangman-game-in-python)

## Code Structure

1. `choose_word(category=None)` - This function chooses a word from the list of categories given in the word_lists dictionary. If no category is provided, it selects a random one.

2. `__init__(self, word)` - This is a constructor method of the HangmanGame class which initializes various attributes like word, display_word, guesses_left, and letters_guessed. It also calls the create_gui() method to create a GUI for the game.

3. `update_display_word(self)`  - This function updates the display_word when a guessed letter is correct.

4. `guess_letter(self, letter)` - This function handles the guessing process by checking if the letter guess is right or wrong based on whether the letter appears in the word or not. If a player guesses all letters correctly, they win. If the guesses run out before the word is guessed, they lose.

5. `create_gui(self)` - This function creates the GUI elements of the game using Tkinter module.

6. `disable_buttons(self)` - This function disables all the letter buttons after the game is over.

7. `update_hangman(self)` - This function updates the hangman image based on the number of guesses left.

8. `change_category(self, category)` - This function changes the category of the word being guessed, destroying the current gui instance and creating a new instance with a fresh word and updated category.

9. `start_game(self)` - This function starts the game loop by continuously updating the window in the mainloop() call.

10. `restart_game(self)` - This function restarts the game by destroying the current GUI instance and creating a new instance with a new word.



<div align="center">
  
## Made with ❤️ , Python, and Tkinter. Enjoy!
  
</div>

