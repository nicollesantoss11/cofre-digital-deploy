from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Cofre Digital Online",
        "environment": os.getenv("ENVIRONMENT", "dev")
    })

@app.route('/segredo')
def segredo():
    senha = os.getenv("SENHA", "não configurada")

    return jsonify({
        "senha_configurada": senha != "não configurada"
    })

if __name__ == "__main__":
    app.run()
