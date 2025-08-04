# Flask Discord Integration

A simple Flask project that allows users to submit messages via a web page. Messages are:

- ✅ Sent to a Discord server via Webhook  
- ✅ Stored in a local SQLite3 database  
- ✅ Viewable through a `/get_messages` endpoint (messages from the last 30 minutes)

---

## 📁 Project Structure

```
flask-discord-project/
│
├── app.py                 # Main Flask app
├── messages.db            # SQLite3 database
├── requirements.txt       # Python package requirements
├── README.md              # Project instructions (this file)
├── .gitignore             # Ignore unnecessary files
└── templates/
    └── index.html         # Frontend form to submit messages
```

---

## 🚀 Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/your-username/flask-discord-project.git
cd flask-discord-project
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your Discord webhook URL

Open the file `app.py` and replace this line:
```python
discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
```

with your actual Discord webhook URL from Discord.

### 4. Run the Flask app
```
python app.py
```

### 5. Open your browser

Go to:
```
http://127.0.0.1:5000/
```

---

## 🔗 Endpoints

- `/` – Main form to submit a message  
- `/input_text` – POST API to send message  
- `/get_messages` – GET API to retrieve messages from the last 30 minutes

---

## ✅ Requirements (in `requirements.txt`)

```
flask
discord-webhook
```

---

## 🛡️ Security Reminder

Never share your Discord webhook publicly. For safety, consider using environment variables or a `.env` file (ask if you want help with that setup).
