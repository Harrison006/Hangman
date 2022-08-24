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
    def get_word(self):
        """
        returns a random word of 3 or more characters
        return: str
        """
        self.cur.execute(
            """
            SELECT word
            FROM Words
            """
        )
        results = self.cur.fetchall()
        return random.choice(results)[0]

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
        self.cur.execute(
        """
        SELECT name
        FROM Users
        """
        )
    #fetch results
    results = self.cur.fetchall()
    # add methods

