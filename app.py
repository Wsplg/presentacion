from flask import Flask, request

app = Flask(__name__)

vocales = ["a", "e", "i", "o", "u"]

@app.route("/")
def home():
    return """
    <h1>🎉 Comprobador de Vocales Guay 🎉</h1>
    <p>Escribe un carácter y pulsa comprobar:</p>
    <form action="/comprobar" method="get">
        <input type="text" name="caracter" maxlength="1" required>
        <button type="submit">Comprobar</button>
    </form>
    <p>Puedes probar letras y ver colores y emojis!</p>
    """

@app.route("/comprobar")
def comprobar():
    caracter = request.args.get("caracter", "").lower()

    if caracter == "":
        return "<p style='color:red;'>No has escrito ningún carácter 😢</p>"

    if caracter in vocales:
        return f"<p style='color:green; font-size:24px;'>✅ {caracter.upper()} es una VOCAL 🎵</p>" \
               "<a href='/'>Volver</a>"
    else:
        return f"<p style='color:blue; font-size:24px;'>❌ {caracter.upper()} NO es una vocal 🚫</p>" \
               "<a href='/'>Volver</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
