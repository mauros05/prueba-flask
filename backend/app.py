from flask import Flask, jsonify, request
from flask_cors import CORS # Para permitir acceso desde REACT 

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir las conexiones desde el frontend

@app.route("/api/secrets", methods=['POST'])
def get_secret():
    data = request.json # JSON recibido desde el frontend
    secret_path =  data.get('path') # La ruta del secreto

    # Simulando un secreto desde Hashicorp Vault
    secrets = {
        "secret/my-secret": { "key1": "value1", "key2": "value2" }
    }
    
    if secret_path in secrets:
        return jsonify(secrets[secret_path]), 200
    return jsonify({"error": "Secret not found"}), 400


# Permite que el servidor corra 
if __name__ == "__main__":
    app.run(debug=True)