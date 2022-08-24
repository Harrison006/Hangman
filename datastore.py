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
