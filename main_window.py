import imp
from pydoc import doc
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from Ui_hangman import Ui_MainWindow
from datastore import Datastore
db = Datastore()

class MainWindow:
    def __init__(self):
        # ui elements
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # init game var
        self.db = Datastore()
        self.user_id = 0
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
    
    def set_button_enabled(self,val):
        #Changing the status of button
        self.ui.a_btn.setEnabled(val)
        self.ui.b_btn.setEnabled(val)
        self.ui.c_btn.setEnabled(val)
        self.ui.d_btn.setEnabled(val)
        self.ui.e_btn.setEnabled(val)
        self.ui.f_btn.setEnabled(val)
        self.ui.g_btn.setEnabled(val)
        self.ui.h_btn.setEnabled(val)
        self.ui.i_btn.setEnabled(val)
        self.ui.j_btn.setEnabled(val)
        self.ui.k_btn.setEnabled(val)
        self.ui.l_btn.setEnabled(val)
        self.ui.m_btn.setEnabled(val)
        self.ui.n_btn.setEnabled(val)
        self.ui.o_btn.setEnabled(val)
        self.ui.p_btn.setEnabled(val)
        self.ui.q_btn.setEnabled(val)
        self.ui.r_btn.setEnabled(val)
        self.ui.s_btn.setEnabled(val)
        self.ui.t_btn.setEnabled(val)
        self.ui.u_btn.setEnabled(val)
        self.ui.v_btn.setEnabled(val)
        self.ui.w_btn.setEnabled(val)
        self.ui.x_btn.setEnabled(val)
        self.ui.y_btn.setEnabled(val)
        self.ui.z_btn.setEnabled(val)       

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
        self.ui.lg_login_btn.clicked.connect(self.login)
        self.ui.lg_register_btn.clicked.connect(self.show_register)
        self.ui.rg_register_btn.clicked.connect(self.register_user)
        
        #letter buttons
        self.ui.a_btn.clicked.connect(lambda: self.letter_btn(self.ui.a_btn))
        self.ui.b_btn.clicked.connect(lambda: self.letter_btn(self.ui.b_btn))
        self.ui.c_btn.clicked.connect(lambda: self.letter_btn(self.ui.c_btn))
        self.ui.d_btn.clicked.connect(lambda: self.letter_btn(self.ui.d_btn))
        self.ui.e_btn.clicked.connect(lambda: self.letter_btn(self.ui.e_btn))
        self.ui.f_btn.clicked.connect(lambda: self.letter_btn(self.ui.f_btn))
        self.ui.g_btn.clicked.connect(lambda: self.letter_btn(self.ui.g_btn))
        self.ui.h_btn.clicked.connect(lambda: self.letter_btn(self.ui.h_btn))
        self.ui.i_btn.clicked.connect(lambda: self.letter_btn(self.ui.i_btn))
        self.ui.j_btn.clicked.connect(lambda: self.letter_btn(self.ui.j_btn))
        self.ui.k_btn.clicked.connect(lambda: self.letter_btn(self.ui.k_btn))
        self.ui.l_btn.clicked.connect(lambda: self.letter_btn(self.ui.l_btn))
        self.ui.m_btn.clicked.connect(lambda: self.letter_btn(self.ui.m_btn))
        self.ui.n_btn.clicked.connect(lambda: self.letter_btn(self.ui.n_btn))
        self.ui.o_btn.clicked.connect(lambda: self.letter_btn(self.ui.o_btn))
        self.ui.p_btn.clicked.connect(lambda: self.letter_btn(self.ui.p_btn))
        self.ui.q_btn.clicked.connect(lambda: self.letter_btn(self.ui.q_btn))
        self.ui.r_btn.clicked.connect(lambda: self.letter_btn(self.ui.r_btn))
        self.ui.s_btn.clicked.connect(lambda: self.letter_btn(self.ui.s_btn))
        self.ui.t_btn.clicked.connect(lambda: self.letter_btn(self.ui.t_btn))
        self.ui.u_btn.clicked.connect(lambda: self.letter_btn(self.ui.u_btn))
        self.ui.v_btn.clicked.connect(lambda: self.letter_btn(self.ui.v_btn))
        self.ui.w_btn.clicked.connect(lambda: self.letter_btn(self.ui.w_btn))
        self.ui.x_btn.clicked.connect(lambda: self.letter_btn(self.ui.x_btn))
        self.ui.y_btn.clicked.connect(lambda: self.letter_btn(self.ui.y_btn))
        self.ui.z_btn.clicked.connect(lambda: self.letter_btn(self.ui.z_btn))

    # ----- slots ----- #
    def new_word_btn(self):
        #chooses new word
        #get new word
        self.choose_word()
        self.display_guesses()

        #reset
        self.misses = 0
        self.display_gallows()
        self.set_button_enabled(True)
        self.ui.result_lb.setText("")

        
    #Letters
    def letter_btn(self,button):
        #disables the clicked button, checks fore letters in the word, checks the state of the game
        #get letter
        guess = button.text().lower()
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
            #check win
            if "_" not in self.guessed_word:
                self.ui.result_lb.setText("Winner!")
        else:
            #add to misses count
            self.misses += 1
            self.display_gallows()
            #check for loss
            if self.misses == 11:
                self.ui.result_lb.setText(f"The word was {self.word.upper()}")
                self.set_button_enabled(False)

    def login(self):
        """
        takes usr name and pasd from ui and checks paswd
        with DB password
        """
        username = self.ui.lg_user_name_le.text()
        password = self.ui.lg_password_le.text()
        stored_password = self.db.get_password(username)
        if stored_password != None:
            if stored_password == password:
                self.user_id = self.db.get_user_id(username)
                self.ui.stackedWidget.setCurrentWidget(self.ui.game_page)
            else:
                self.ui.lg_message_lb.setText("Wrong password")
        else:
            self.ui.lg_message_lb.setText("user not registered")


    def show_register(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.register_page)


    def register_user(self):
        """
        Adding user to databse if username is not taken
        """
        user_name = self.ui.rg_user_name_le.text()
        password = self.ui.rg_password_le.text()
        
        if user_name in self.db.get_all_usernames():
            self.ui.rg_message_lb("Username is taken")
        if len(password) < 6 or len(password) > 20:
            self.ui.rg_message_lb("Password is trash")
        else:
            self.db.add_credentials(user_name, password)
            self.user_id = self.db.get_user_id(user_name)
            self.ui.stackedWidget.setCurrentWidget(self.ui.game_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())