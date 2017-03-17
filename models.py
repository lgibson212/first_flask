#!/usr/bin/env python3

import sqlite3
# import wrapper
from datetime import datetime

connection = sqlite3.connect('twitter_clone.db', check_same_thread=False)
cursor = connection.cursor()

class User():

    @classmethod
    def register(cls, uname, pword):
        cursor.execute("""
            SELECT * FROM users WHERE username = ?;
        """, (uname,)) #needs to be a tuple
        result = cursor.fetchone();
        if result: #if find someone, return false- pass to controller
            return False
        else: #create new user into db
            cursor.execute("""
            INSERT INTO users(username, password) VALUES (?, ?);
        """, (uname, pword) 
            )
            connection.commit()
            print("new user created")
            return True #cursor.lastrowid()

    @classmethod
    def login(cls, uname, pword):
        username=cursor.execute("""SELECT * FROM users WHERE username = ?;""", (uname,))
        username = cursor.fetchone();
        password=cursor.execute("""SELECT * FROM users WHERE password = ?;""", (pword,))
        password = cursor.fetchone();

        if username: #if find someone, return user ID- pass to controller
            if password:
                return True #cursor.lastrowid()
        else: #if not found, send to controller and register.
            return False
    
        # cursor.execute('SELECT username FROM users WHERE username=?;', (username,))
        # stored_username = cursor.fetchone()
        # if stored_username:
        #     cursor.execute('SELECT password FROM users WHERE username=?;', (username,))
        #     stored_password = cursor.fetchone()
        #     if stored_password[0] == password:
        #         return True
        #     else:
        #         prng = random.randint(1, 128)
        #         fuzz = float(prng / 1000)
        #         time.sleep(fuzz)    
        #         return False            
        # else:
        #     prng = random.randint(1, 128)
        #     fuzz = float(prng / 1000)
        #     time.sleep(fuzz)    
        #     return False
    @classmethod
    def get_id(cls, username):
        cursor.execute("""SELECT id FROM users WHERE username = ?;""", (username,))
        user_id = cursor.fetchall() #returns tuple
        return user_id[0]

class Tweet():

    @classmethod
    def publ(cls):
        cursor.execute('''SELECT post FROM tweets;''')
        all_tweets = cursor.fetchall()
        return all_tweets


    @classmethod
    def priv(cls, username):
        cursor.execute('''SELECT id FROM users WHERE username=?;''', (username,))
        user_id = cursor.fetchone()
        cursor.execute('''SELECT post FROM tweets WHERE user_id=?;''', (user_id[0],)) #user_id is a tuple (x,)
        user_tweets = cursor.fetchall()
        return user_tweets


    @classmethod
    def store_tweet(cls, post, user_id):
        print(post, user_id)
        time=datetime.now()
        cursor.execute('''INSERT INTO tweets (postTime, post, user_id) VALUES (?, ?, ?);
        ''', (time, post, user_id[0]) 
            )
        connection.commit()
        print("new tweet created")
        return True #cursor.lastrowid()


### writing the tweet from the database
### reading the tweet from the database
##