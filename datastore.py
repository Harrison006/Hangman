
import random
import sqlite3
from unittest import result
class Datastore():
    def __init__(self):
        """
        intialise datastore by connecting to the sqlite db
        """
        db_file = "hangman_datastore.db"
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

#get the stuff

    def get_word(self):
        """
        returns a random word of 3 or more characters
        return: str
        """
        self.cur.execute(
            """
            SELECT word_id, word
            FROM Words
            """
        )
        results = self.cur.fetchall()
        
        while True:
            word = random.choice(results)
            if len(word[1]) > 3:
                return word



    def get_password(self,user):
        """
        retrieves users password
        user:str
        Password:str
        """
        self.cur.execute(
            """
            SELECT password
            FROM Users
            WHERE name = :user
            """,
            {
                "user":user
            }
        )
        results = self.cur.fetchone()
        if results is None:
            return None
        else:
            return results[0]

    def get_user_id(self, user):
        """
        returns the user_id for the provided user
        name:str
        user_id: int
        """
        self.cur.execute(
            """
            SELECT user_id
            FROM Users
            WHERE name = :name
            """,
            {
                "name":user
            }
        )
        results = self.cur.fetchone()
        if results is None:
            return None
        else:
            return results[0]

    def get_all_usernames(self):
        """
        retrieves all usernames
        return: [str]
        """
        #exe sql
        self.cur.execute(
        """
        SELECT name
        FROM Users
        """
    )
        results = self.cur.fetchall()
        users = []
        for value in results:
            users.append(value[0])

        return users


    def get_guessed_words(self, user_id):
        """
        retrieve list of guessed words
        user_id: int
        return [str]
        """
        self.cur.execute(
            """
            SELECT word
            FROM Words
            WHERE word_id IN (
                SELECT word_id
                FROM Games
                WHERE user_id = :user_id AND guessed = "TRUE"
            )
            """,
            {
                "user_id":user_id
            }
        )
        results = self.cur.fetchall()
        
        if results == []:
            return results
        else:
            words = []
            for value in results:
                words.append(value[0])
            return words

    def get_games_played(self, user_id):
        """
        Returns all games played
        user_id = int
        """

        self.cur.execute(
            """
            SELECT COUNT(user_id)
            FROM  Games
            WHERE user_id = :user_id
            """,
            {
                "user_id":user_id
            }
        )

        results = self.cur.fetchone()

        return results[0]


    def get_games_won(self, user_id):
        """
        Get all games won
        user_id = int
        """
        
        self.cur.execute(
            """
            SELECT COUNT(user_id)
            FROM Games
            WHERE user_id = :user_id AND guessed = "TRUE"
            """,
            {
                "user_id":user_id
            }
        )

        results = self.cur.fetchone()
        return results[0]


    def get_most_missed(self, user_id):
        """
        returns most missed word
        user_id = int
        """

        self.cur.execute(
            """
            SELECT word
            FROM Words
            WHERE word_id IN (
                SELECT word_id
                FROM Games
                WHERE user_id = :user_id AND guessed = "FALSE"
                GROUP BY word_id 
                ORDER BY COUNT(word_id) DESC
                LIMIT 1
            )
            """,
            {
                "user_id":user_id
            }
        )
        results = self.cur.fetchone()
        
        if results == None:
            return None
        else:
            return results[0]


    def get_longest_word(self, user_id):
        """
        Returns longest word user guessed
        user_id = int
        """

        self.cur.execute(
            """
            SELECT word
            FROM Words
            WHERE word_id IN (
                SELECT word_id
                FROM Games
                WHERE user_id = :user_id AND guessed = "TRUE"
            )
            ORDER BY LENGTH(word) DESC
            """,
            {
                "user_id":user_id
            }
        )
        results = self.cur.fetchone()
        
        if results == None:
            return None
        else:
            return results[0]

        

    def get_username(self, user_id):
            """
            Gets Username
            user_id = int
            """

            self.cur.execute(
                """
                SELECT name
                FROM Users
                WHERE user_id = :user_id
                """,
                {
                    "user_id":user_id
                }
            )    

            results = self.cur.fetchone()
            return results[0]

    # add methods






    def add_credentials(self,username,password):
        """
        sending user credentials to the datastore
        user_name: str
        password: str
        """
        self.cur.execute(
            """
            INSERT INTO Users (name,password)
            VALUES (:username,:password)
            """,
            {
                "username":username,
                "password":password
            }
        )
        #commit 
        self.conn.commit()


    def add_result(self, user_id, word_id, guessed):
        """
        Adding Results to db
        user_id = int
        word_id = int
        guess = str
        """

        self.cur.execute(
            """
            INSERT INTO Games (user_id, word_id, guessed)
            VALUES (:user_id, :word_id, :guessed)
            """,
            {
                "user_id":user_id,
                "word_id":word_id,
                "guessed":guessed
            }
        )

        self.conn.commit()
