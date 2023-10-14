from flask import Flask, render_template, request

import psycopg2

# initialize the app
app = Flask(__name__)
conn = None


def get_db_connection():
    conn = psycopg2.connect(host='db',
                        database='portfolio',
                        user="aerielellis",
                        password="password123",
                        port="5432")
    return conn

conn = get_db_connection()    
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS connections (id serial PRIMARY KEY, first_name varchar(100), last_name varchar(100), email varchar(100), message varchar(100));''' )
cur.execute('''CREATE TABLE IF NOT EXISTS projects (id serial PRIMARY KEY, name varchar(100), description varchar(100), likes int, comments text);''' )
conn.commit()
cur.close()
conn.close()






if __name__ == '__main__':
    # we want the server to keep reloading since we are in developerment so we keep this to true
    # app.debug = True
    app.run(port=3000, host="0.0.0.0")