from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "clave_super_secreta"  # NECESARIO para usar session


@app.route("/")
def home():
    return render_template("index.html")
  



# ---------
# JUEGO: Adivina el número
# ---------

MINIMO = 1
MAXIMO = 10
num = random.randint(MINIMO, MAXIMO)

@app.route("/adivinar", methods=["GET", "POST"])
def adivinar():
    global num
    mensaje = ""
    
    if request.method == "POST":
        intento = int(request.form["numero"])
        if intento < num:
            mensaje = "El número es mayor."
        elif intento > num:
            mensaje = "El número es menor."
        else:
            mensaje = "🎉 ¡Felicidades! Has adivinado el número."
            num = random.randint(MINIMO, MAXIMO)  # reinicia el juego
    
    return render_template("adivinar.html", mensaje=mensaje)

#----------
# JUEGO: El ahorcado
#----------
MAX_INTENTOS = 6

palabras = [
    "JUEGO",
    "CONSOLA",
    "MANDO",
    "NIVEL",
    "VIDA",
    "PANTALLA",
    "PIXEL",
    "SONIDO",
    "GRAFICO",
    "JUGADOR",
    "ENEMIGO",
    "ESPADA",
    "TESORO",
    "MISION",
    "ONLINE",
    "MULTIJUGADOR",
    "VENTAJA",
    "DERROTA",
    "VICTORIA",
    "MAPA",
    "ORDENADOR",
    "PROGRAMA",
    "CODIGO",
    "VARIABLE",
    "FUNCION",
    "ALGORITMO",
    "RED",
    "SERVIDOR",
    "USUARIO",
    "CLAVE",
    "TECLADO",
    "RATON",
    "MONITOR",
    "INTERNET",
    "CORREO",
    "ARCHIVO",
    "CARPETA",
    "DISCO",
    "MEMORIA",
    "CHIP",
    "PROCESADOR",
    "GRAFICA",
    "ROBOT",
    "ANDROID",
    "DRIVER",
    "VENTANA",
    "NUBE",
    "SEGURIDAD",
    "BROWSER",
    "APP"
]


@app.route("/ahorcado", methods=["GET", "POST"])
def ahorcado():
    if "palabra" not in session:  
        # Si no hay partida, crear una nueva
        session["palabra"] = random.choice(palabras)
        session["letras_correctas"] = []
        session["letras_incorrectas"] = []

    palabra = session["palabra"]
    letras_correctas = session["letras_correctas"]
    letras_incorrectas = session["letras_incorrectas"]

    # Inicializa las variables
    mensaje = None
    fin = False

    if request.method == "POST":
        letra = request.form["letra"].upper()

        if letra in palabra:
            if letra not in letras_correctas:
                letras_correctas.append(letra)
        else:
            if letra not in letras_incorrectas:
                letras_incorrectas.append(letra)

        # Guardar en sesión
        session["letras_correctas"] = letras_correctas
        session["letras_incorrectas"] = letras_incorrectas

    # Mostrar la palabra con guiones bajos
    mostrar = "".join([l if l in letras_correctas else "_ " for l in palabra])

    # Si es una victoria
    if "_" not in mostrar:
        mensaje = "🎉 ¡Felicidades! Has adivinado la palabra."
        fin = True

    # Si es una derrota
    elif len(letras_incorrectas) >= MAX_INTENTOS:
        mensaje = f"😞 Has perdido. La palabra era {palabra}."
        fin = True

    return render_template(
        "ahorcado.html",
        palabra=mostrar,
        letras_incorrectas=letras_incorrectas,
        mensaje=mensaje,
        fin=fin,
    )

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

@app.route("/reiniciar_ahorcado")
def reiniciar_ahorcado():
    session.clear()
    return redirect(url_for("ahorcado"))

if __name__ == "__main__":
    app.run(debug=True)
