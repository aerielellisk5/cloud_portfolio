"Adding some text here to pass the test"
from flask import Flask, render_template, request

import psycopg2

# initialize the app
app = Flask(__name__)
conn = None


def get_db_connection():
    """Connecting to the database"""
    # conn = psycopg2.connect(host='db',
    #                     database='portfolio',
    #                     user="aerielellis",
    #                     password="password123",
    #                     port="5432")
    
    conn = psycopg2.connect(host='database-2.cutddukdl6vf.us-east-1.rds.amazonaws.com',
                        database='portfolio',
                        user="aerielellis",
                        password="password123",
                        port="5432")
    return conn

conn = get_db_connection()
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS connections (id serial PRIMARY KEY, project_name varchar(100), like_count int);''' )
cur.execute('''CREATE TABLE IF NOT EXISTS comments (id serial PRIMARY KEY, name varchar(100),  comments text);''' )
cur.execute('''CREATE TABLE IF NOT EXISTS counter (id serial PRIMARY KEY, counter int);''')
conn.commit()
cur.close()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')






if __name__ == '__main__':
    # we want the server to keep reloading since we are in developerment so we keep this to true
    # app.debug = True
    app.run(port=3000, host="0.0.0.0")
    