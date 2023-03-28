import random
import tkinter as tk

word_lists = {
    "fruits": ["apple", "banana", "orange", "kiwi", "pineapple"],
    "coding": ["python", "java", "javascript", "php", "ruby", "html", "css"],
}

# Function to choose a word from the list
def choose_word(category=None):
    if category is None:
        # Choose a random category and word
        category = random.choice(list(word_lists.keys()))
    word_list = word_lists[category]
    return random.choice(word_list)

# Class for the game
class HangmanGame:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = 6
        self.letters_guessed = []
        # Choose a random index to fill in the guess
        guess_index = random.randint(0, len(self.word) - 1)
        self.display_word = "-" * len(self.word)
        self.display_word = self.display_word[:guess_index] + self.word[guess_index] + self.display_word[guess_index+1:]
        
        self.create_gui()

    # Function to update the display word when a letter is guessed correctly
    def update_display_word(self):
        new_display_word = ""
        for i in range(len(self.word)):
            if self.word[i] == self.display_word[i]:
                new_display_word += self.word[i]
            elif self.word[i] in self.letters_guessed:
                new_display_word += self.word[i]
            else:
                new_display_word += "-"
        self.display_word = new_display_word
        self.word_label.config(text=self.display_word)

    # Function to handle a letter guess
    def guess_letter(self, letter):
        if letter in self.letters_guessed:
            self.info_label.config(text="You already guessed that letter!")
        else:
            self.letters_guessed.append(letter)
            if letter in self.word:
                self.update_display_word()
                if "-" not in self.display_word:
                    self.info_label.config(text="Congratulations, you won!")
                    self.disable_buttons()
            else:
                self.guesses_left -= 1
                self.info_label.config(text="Sorry, wrong letter!")
                self.update_hangman()
                if self.guesses_left == 0:
                    self.info_label.config(text="Sorry, you lost! The word was {}".format(self.word))
                    self.disable_buttons()

    # Function to create the GUI
    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Hangman")
        
        # Create a dropdown menu for selecting category
        self.category_var = tk.StringVar()
        self.category_var.set("Select category")
        categories = ["All"] + list(word_lists.keys())
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *categories, command=self.change_category)
        self.category_menu.grid(row=0, column=0, columnspan=2)

        self.canvas = tk.Canvas(self.root, width=200, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.images = [
            tk.PhotoImage(file="hangman/hangman0.png"),
            tk.PhotoImage(file="hangman/hangman1.png"),
            tk.PhotoImage(file="hangman/hangman2.png"),
            tk.PhotoImage(file="hangman/hangman3.png"),
            tk.PhotoImage(file="hangman/hangman4.png"),
            tk.PhotoImage(file="hangman/hangman5.png"),
            tk.PhotoImage(file="hangman/hangman6.png"),
        ]
        self.hangman_image = self.canvas.create_image(100, 110, image=self.images[0])

        self.word_label = tk.Label(self.root, text=self.display_word, font=("Arial", 24))
        self.word_label.grid(row=2, column=0, columnspan=2)

        self.info_label = tk.Label(self.root, text="Guess a letter!", font=("Arial", 16))
        self.info_label.grid(row=3, column=0, columnspan=2)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=4, column=0, columnspan=2)
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, bg="green", fg="white", font=("Arial", 16), relief="ridge")
        self.restart_button.grid(row=5, column=0, columnspan=2)


        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # Generate random colors for each button
            bg_color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
            fg_color = 'white' if int(bg_color[1:], 16) > 0xffffff/2 else 'black'
            
            # Create the button with the random colors
            button = tk.Button(self.button_frame, text=letter, width=3, bg=bg_color, fg=fg_color, command=lambda l=letter: self.guess_letter(l))
            button.pack(side="left")

    # Function to disable all letter buttons
    def disable_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")

    # Function to update the hangman image when a letter is guessed incorrectly
    def update_hangman(self):
        self.canvas.itemconfig(self.hangman_image, image=self.images[6-self.guesses_left])
    
    def change_category(self, category):
        word = choose_word(None if category == "All" else category)
        self.root.destroy()
        game = HangmanGame(word)
        game.start_game()
    

    # Function to start the game loop
    def start_game(self):
        self.root.mainloop()

    def restart_game(self):
        self.root.destroy()
        word = choose_word()
        self.__init__(word)
        self.start_game()


# Start the game by choosing a word and creating a HangmanGame object
word = choose_word()
game = HangmanGame(word)
game.start_game()
