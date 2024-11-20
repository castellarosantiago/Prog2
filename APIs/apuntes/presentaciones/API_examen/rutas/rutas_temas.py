from flask import Blueprint, request, jsonify
from modelos.entidades.tema import Tema
from modelos.repositorios.repositorios import obtenerRepoTemas

repo_temas = obtenerRepoTemas()

bp_temas = Blueprint("bp_temas", __name__)

@bp_temas.route("/temas", methods=["GET"])
def buscar_todos():
    lista_dicc=[]
    for tema in repo_temas.obtenerTodos():
        lista_dicc.append(tema.toDiccionario())
    return jsonify(lista_dicc), 200

@bp_temas.route("/temas/<int:numero>", methods=["GET"])
def buscar_por_numero(numero):
    tema_encontrado = repo_temas.obtenerTemaPorNumero(numero)
    if tema_encontrado != None:
        return jsonify(tema_encontrado.toDiccionario()), 200
    else:
        return jsonify({"Error":"No se encontró el tema con ese numero"}), 404
    
@bp_temas.route("/temas", methods=["POST"])
def crear_tema():
    if request.is_json:
        diccDatos = request.get_json()
        if "numero" in diccDatos and "nombre" in diccDatos and "enunciado" in diccDatos:
            tema_nuevo = Tema.fromDiccionario(diccDatos)
            if not repo_temas.existeNumero(tema_nuevo.obtenerNumero()):
                if repo_temas.agregar(tema_nuevo):
                    return jsonify({"mensaje":"Tema agregado con éxito", "tema":tema_nuevo.toDiccionario()}), 201
                else:
                    return jsonify({"error":"No se puedo agregar el tema"}),400
            else:
                return jsonify({"error":"Ya existe un tema con ese numero"}),400
        else:
            return jsonify({"error":"Faltan datos en el json, debe tener 'numero', 'nombre' y 'enunciado'"}),400
    else:
        return jsonify({"error":"Debe enviar los datos en JSON"}),400