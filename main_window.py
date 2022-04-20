import imp
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from Ui_hangman import Ui_MainWindow
from datastore import Datastore

class MainWindow:
    def __init__(self):
        # ui elements
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # init game var
        self.db = Datastore()
        self.word = ''
        self.guessed_word = []
        self.misses = 0
        # init ui with start values
        self.choose_word()
        self.display_guesses()
        self.display_gallows()
        self.signals()

    def show(self):
        self.main_win.show()

    def choose_word(self):
        # gets word from datastore
        
        self.word = self.db.get_word()
        self.guessed_word = ["_"] * len(self.word)

    def display_guesses(self):
        # Display Letters missed
        display_word = ""
        for charater in self.guessed_word:
            display_word = display_word + charater + " "

        self.ui.word_lb.setText(display_word)

    def display_gallows(self):
        #displays the lil hangman pictures
        file_name = (f"./assets/{self.misses}.png")
        gallow = QPixmap(file_name)
        self.ui.gallow_lb.setPixmap(gallow)
         
    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        # control buttons
        self.ui.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.new_word_btn.clicked.connect(self.new_word_btn)
        
        #letter buttons
        self.ui.a_btn.clicked.connect(lambda: self.letter_btn(self.ui.a_btn))
    # ----- slots ----- #
    def new_word_btn(self):
        #chooses new word
        #get new word
        self.choose_word()
        self.display_guesses()
        #reset
        self.misses = 0
        self.display_gallows()
    #Letters

    def letter_btn(self,button):
        #disables the clicked button, checks fore letters in the word, checks the state of the game
        #get letter
        guess = button.text().lower()
        print(guess)
        #disabled letter
        button.setEnabled(False)
        #check if letter in the word
        if guess in self.word:
            #add guess
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.guessed_word[index] = guess.upper()
            #display the word
            self.display_guesses()
        else:
            #add to misses count
            self.misses += 1
            self.display_gallows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())