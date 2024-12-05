from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Подключение к базе данных
def get_books():
    connection = sqlite3.connect("database_lab10.db")
    cursor = connection.cursor()
    cursor.execute("SELECT books.title, authors.name FROM books INNER JOIN authors ON books.author_id = authors.id")
    rows = cursor.fetchall()
    connection.close()
    return [{"title": row[0], "author": row[1]} for row in rows]

@app.route('/books', methods=['GET'])
def books():
    return jsonify(get_books())

if __name__ == '__main__':
    app.run(debug=True)