from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    data = request.json
    text = data.get("text", "")
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": text}]
    )
    
    output = response.choices[0].message.content
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
