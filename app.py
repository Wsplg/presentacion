from flask import Flask, request, jsonify

app = Flask(__name__)

vocales = ["a", "e", "i", "o", "u"]

@app.route("/")
def home():
    return (
        "Servicio activo.<br>"
        "Usa /comprobar?caracter=a para probar."
    )

@app.route("/comprobar")
def comprobar():
    caracter = request.args.get("caracter", "")

    if caracter == "":
        return jsonify(error="No has enviado ningún carácter")

    if caracter == " ":
        return jsonify(resultado="Se termina la comprobación")

    if caracter.lower() in vocales:
        return jsonify(
            caracter=caracter,
            resultado="VOCAL"
        )
    else:
        return jsonify(
            caracter=caracter,
            resultado="NO VOCAL"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
