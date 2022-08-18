#datastore
import random
import sqlite3
class Datastore():

    def __init__(self):
        """
        connect sqlite db
        """
        db_file = "hangman_datastore.db"
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
    def get_word(self):
        #returns random word of 3 or more char
        word = ""
        while len(word) < 3:
            word = random.choice(self.words)
        return word
