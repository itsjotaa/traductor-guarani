# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from translator.traductor import traducir

app = Flask(__name__)

@app.route("/translate", methods=["POST", "GET"])  # ← Agregar GET
def translate_text():
    # Determinar si es POST o GET
    if request.method == "POST":
        data = request.json
        if not data or "text" not in data:
            return jsonify({"error": "Falta el campo 'text' en JSON"}), 400
        texto_espanol = data["text"]
    else:  # GET
        texto_espanol = request.args.get("texto", "")
        if not texto_espanol:
            return jsonify({"error": "Usa: /translate?texto=tu frase aquí"}), 400

    texto_guarani = traducir(texto_espanol)

    return jsonify({
        "original": texto_espanol,
        "traducido": texto_guarani,
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "Traducir Español-Guaraní API",
        "endpoints": {
            "POST /translate": "Traducir texto (JSON)",
            "GET /translate?texto=frase": "Traducir desde navegador",
            "GET /health": "Estado del servicio"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK", "proyecto": "traductor-guarani"})

if __name__ == "__main__":
    print("Iniciando API del traductor...")
    print("URL: http://localhost:5000")
    print("Para traducir: http://localhost:5000/translate?texto=hola amigos")
    app.run(debug=True, host="0.0.0.0", port=5000)