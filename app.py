from flask import Flask, jsonify, request
from supabase import create_client
import os

# Initialize Flask app
app = Flask(__name__)

# Validate Supabase credentials
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("❌ Missing SUPABASE_URL or SUPABASE_KEY in environment variables.")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 🏠 Home Page
@app.route("/", methods=["GET"])
def home():
    return """
    <h1>📚 Kamal Library Virtual Assistant</h1>
    <p>Welcome to the AI-powered Kamal Library system!</p>
    <ul>
        <li><a href="/books">📘 View All Books</a></li>
        <li><a href="/users">👤 View All Users</a></li>
        <li><a href="/transactions">📄 View All Transactions</a></li>
    </ul>
    <p>POST to <code>/borrow</code> to borrow a book.</p>
    """

# 📘 Get All Books
@app.route("/books", methods=["GET"])
def get_books():
    try:
        response = supabase.table("books").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 👤 Get All Users
@app.route("/users", methods=["GET"])
def get_users():
    try:
        response = supabase.table("users").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📄 Get All Transactions
@app.route("/transactions", methods=["GET"])
def get_transactions():
    try:
        response = supabase.table("transactions").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📥 Borrow a Book
@app.route("/borrow", methods=["POST"])
def borrow_book():
    try:
        data = request.get_json()
        # Expecting keys: user_id, book_id, borrow_date (YYYY-MM-DD)
        if not all(key in data for key in ["user_id", "book_id", "borrow_date"]):
            return jsonify({"error": "Missing required fields."}), 400

        response = supabase.table("transactions").insert(data).execute()
        return jsonify({"message": "Book borrowed successfully!", "transaction": response.data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask server
if __name__ == "__main__":
    app.run(host="
