import sqlite3


# Create a database
connection = sqlite3.connect('twitter_clone.db')
cursor = connection.cursor()


# Create a table for the User class in the model
cursor.execute('''
    DROP TABLE IF EXISTS users;
''')

cursor.execute('''
    CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
    );
''')

# Create another table for the Tweets class in the model
cursor.execute('''
    DROP TABLE IF EXISTS tweets;
''')

cursor.execute('''
    CREATE TABLE tweets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    postTime TEXT,
    post VARCHAR(140),
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
    );
''')

connection.commit()
connection.close()