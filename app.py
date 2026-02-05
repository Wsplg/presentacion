@app.route("/comprobar")
def comprobar():
    caracter = request.args.get("caracter", "").lower()

    if caracter == "":
        return "<p style='color:red;'>No has escrito ningún carácter</p>"

    # Si es un punto
    if caracter == ".":
        return "<p style='color:red; font-size:24px;'>Ten por el culo ancor</p>" \
               "<a href='/'>Volver</a>"

    # Comprobar si es letra
    if not caracter.isalpha():
        return f"<p style='color:orange; font-size:24px;'>{caracter} no es una letra</p>" \
               "<a href='/'>Volver</a>"

    if caracter in vocales:
        return f"<p style='color:green; font-size:24px;'>{caracter.upper()} es una VOCAL</p>" \
               "<a href='/'>Volver</a>"
    else:
        return f"<p style='color:blue; font-size:24px;'>{caracter.upper()} NO es una vocal</p>" \
               "<a href='/'>Volver</a>"
