from flask import Flask, render_template, request
import random
import os

app = Flask(__name__, template_folder='templates')

# Lista de opciones: piedra, papel, tijeras
opciones = ['piedra', 'papel', 'tijeras']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jugar', methods=['POST'])
def jugar():
    eleccion_jugador = request.form['eleccion'].lower()

    if eleccion_jugador not in opciones:
        return "Opción no válida. Por favor, elige entre piedra, papel o tijeras."

    eleccion_oponente = random.choice(opciones)
    resultado = determinar_ganador(eleccion_jugador, eleccion_oponente)

    return render_template('resultado.html', eleccion_jugador=eleccion_jugador, eleccion_oponente=eleccion_oponente, resultado=resultado)

def determinar_ganador(jugador, oponente):
    # Lógica para determinar el ganador
    if jugador == oponente:
        return "Empate"
    elif (jugador == 'piedra' and oponente == 'tijeras') or (jugador == 'tijeras' and oponente == 'papel') or (jugador == 'papel' and oponente == 'piedra'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

if __name__ == '__main__':
    app.run(debug=True)
