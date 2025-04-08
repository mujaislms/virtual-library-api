from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)
# Route: Home
@app.route("/")
def index():
    return jsonify({"message": "Welcome to Virtual Library Assistant API 🚀"})

# Route: Get all books
@app.route("/books", methods=["GET"])
def get_books():
    response = supabase.table("books").select("*").execute()
    return jsonify(response.data)

# Route: Get all users
@app.route("/users", methods=["GET"])
def get_users():
    response = supabase.table("users").select("*").execute()
    return jsonify(response.data)

# Route: Borrow a book
@app.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.get_json()
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    # Insert a transaction
    transaction = {
        "user_id": user_id,
        "book_id": book_id,
        "status": "borrowed"
    }
    response = supabase.table("transactions").insert(transaction).execute()
    return jsonify({"message": "Book borrowed successfully", "transaction": response.data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
