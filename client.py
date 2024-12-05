import tkinter as tk
import requests

def fetch_books():
    try:
        response = requests.get("http://127.0.0.1:5000/books")
        books = response.json()
        result_text.delete(1.0, tk.END)
        for book in books:
            result_text.insert(tk.END, f"Book: {book['title']}, Author: {book['author']}\n")
    except requests.exceptions.ConnectionError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Could not connect to server.")

# Настройка интерфейса
root = tk.Tk()
root.title("Books Viewer")

fetch_button = tk.Button(root, text="Fetch Books", command=fetch_books)
fetch_button.pack()

result_text = tk.Text(root, height=20, width=50)
result_text.pack()

root.mainloop()