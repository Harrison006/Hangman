#datastore
import random
class Datastore():

    def __init__(self):
        """
        initialise datastore by reading dictionary file and adding each word into a list 
        """

        with open("dictionary.txt") as word_file:
            self.words = word_file.read().splitlines()
        print(self.words)
    def get_word(self):
        #returns random word of 3 or more char
        word = ""
        while len(word) < 3:
            word = random.choice(self.words)
        return word
