from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre': 'Mi Aplicación Flask',
        'versión': '1.0',
        'descripción': 'Esta es una aplicación simple con rutas GET y POST.'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    nombre = data.get('nombre', 'invitado')
    return jsonify({
        'respuesta': f'Hola, {nombre}. ¡Gracias por tu mensaje!'
    })

if __name__ == '__main__':
    app.run(debug=True)
