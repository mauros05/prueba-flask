from flask import Flask, jsonify, request
from flask_cors import CORS # Para permitir acceso desde REACT 

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir las conexiones desde el frontend

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Permite que el servidor corra 
if __name__ == "__main__":
    app.run(debug=True)