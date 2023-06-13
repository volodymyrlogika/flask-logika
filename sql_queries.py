import sqlite3

def open():
    global conn, cursor
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def add_category(data):
    open()
    cursor.execute('''
    INSERT INTO category (name) VALUES ((?))''', [data] )
    conn.commit()
    close()

def add_user(*data):
    open()
    cursor.execute('''
    INSERT INTO users (name, email, password) VALUES ((?), (?), (?))''', [data[0], data[1], data[2]] )
    conn.commit()
    close()

def get_posts():
    open()
    cursor.execute('''SELECT * from posts''')
    posts = cursor.fetchall()
    conn.commit()
    close()
    return posts

print(get_posts())