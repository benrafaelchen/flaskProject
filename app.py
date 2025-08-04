from flask import Flask, render_template, request, jsonify
from discord_webhook import DiscordWebhook
import sqlite3
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__)


# Set up SQLite database connection
def get_db_connection():
    conn = sqlite3.connect("messages.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create messages table if it doesn't exist
with get_db_connection() as conn:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()

# Discord webhook URL (replace with your actual webhook URL)
discord_webhook_url = "https://discord.com/api/webhooks/1357035269227806840/0Ormx3gHeQhI9lR3jnwtzs0Vb0232iAmnGET9-mZ9t6Mj0wuk7rNVh21hAUGob0-MF4f"


# Endpoint 1 - Receive text input
@app.route("/input_text", methods=["POST"])
def input_text():
    try:
        data = request.get_json()
        text = data["text"]

        # Send the message to Discord
        send_to_discord(text)

        # Save the message to the database
        save_to_database(text)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# Endpoint 2 - Send message to Discord
def send_to_discord(text):
    webhook = DiscordWebhook(url=discord_webhook_url, content=text)
    webhook.execute()


# Save message to SQLite database
def save_to_database(text):
    with get_db_connection() as conn:
        conn.execute("INSERT INTO messages (content) VALUES (?)", (text,))
        conn.commit()


# Endpoint 3 - Retrieve messages from the last 30 minutes
@app.route("/get_messages", methods=["GET"])
def get_messages():
    try:
        cutoff_time = datetime.now() - timedelta(minutes=30)
        with get_db_connection() as conn:
            cursor = conn.execute(
                "SELECT content, timestamp FROM messages WHERE timestamp >= ?",
                (cutoff_time,),
            )
            messages = [
                {"content": row["content"], "timestamp": row["timestamp"]}
                for row in cursor.fetchall()
            ]
        return jsonify({"status": "success", "messages": messages})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# Root endpoint - Serve HTML form
@app.route("/")
def index():
    return render_template("index.html")


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
