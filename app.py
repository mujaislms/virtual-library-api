from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Load Supabase credentials from environment variables
#SUPABASE_URL = os.getenv("https://zsikmtnlzwzcdoxblztx.supabase.co")
#SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpzaWttdG5send6Y2RveGJsenR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIyMTU5NjcsImV4cCI6MjA1Nzc5MTk2N30.yDWFD3iB_fWiPslmFLd5BgUJ8GRYxPvUvEgqSW7JX4c")
#supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Route: Home
@app.route("/")
def index():
    return jsonify({"message": "Welcome to Kamal Library API 🚀"})

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
