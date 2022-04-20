import imp
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
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
        pass
    
    # ----- slots ----- #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())