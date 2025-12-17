from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

@app.route("/submit", methods=["POST"])
def submit_result():
    data = request.json
    wpm = data.get("wpm")
    accuracy = data.get("accuracy")

    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO results (wpm, accuracy) VALUES (%s, %s)",
        (wpm, accuracy)
    )
    db.commit()
    db.close()

    return jsonify(message="Result stored successfully")

@app.route("/health")
def health():
    return "OK"
