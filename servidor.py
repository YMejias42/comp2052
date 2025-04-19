from flask import Flask, request, jsonify
import platform

app = Flask(__name__)

# Lista para almacenar usuarios
usuarios = []

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    sistema_info = {
        'sistema': platform.system(),
        'version': platform.version(),
        'plataforma': platform.platform()
    }
    return jsonify(sistema_info), 200

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    correo = datos.get('correo')

    if not nombre or not correo:
        return jsonify({'error': 'Faltan datos: nombre y/o correo'}), 400

    usuario = {'nombre': nombre, 'correo': correo}
    usuarios.append(usuario)
    return jsonify({'mensaje': 'Usuario creado exitosamente', 'usuario': usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

if __name__ == '__main__':
    app.run(debug=True)
