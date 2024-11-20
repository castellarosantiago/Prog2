from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoAlumnos
from modelos.entidades.alumno import Alumno

repo_alumnos = obtenerRepoAlumnos()

bp_alumnos = Blueprint("bp_alumnos", __name__)

#VALIDACIONES!!
@bp_alumnos.route("/alumnos", methods=["GET"])
def obtener_todos():
    # return jsonify([alumno.toDiccionario() for alumno in repo_alumnos.obtenerTodos()])
    lista_dicc = []
    for alumno in repo_alumnos.obtenerTodos():
        lista_dicc.append(alumno.toDiccionario())
    return jsonify(lista_dicc), 200

#VALIDACIONES!!
@bp_alumnos.route("/alumnos/<int:legajo>", methods = ["GET"])
def obtener_alumno_por_legajo(legajo):
    alumno_encontrado = repo_alumnos.obtenerAlumnoPorLegajo(legajo)
    if alumno_encontrado != None:
        return jsonify({"mensaje":"Alumno encontrado", "alumno":alumno_encontrado.toDiccionario()}), 200
    else:
        return jsonify({"error":"Alumno no encontrado"}), 404

@bp_alumnos.route("/alumnos", methods =["POST"])  
def agregar():
    if request.is_json:
        diccDatos = request.get_json()
        if "legajo" in diccDatos and "nombre" in diccDatos and "apellido" in diccDatos:
            #continuo
            alumno_creado = Alumno.fromDiccionario(diccDatos)
            # alumno_creado_V2 = Alumno(diccDatos["legajo"], diccDatos["apellido"], diccDatos["nombre"])
            if repo_alumnos.existeAlumnoPorLegajo(alumno_creado.obtenerLegajo()):
                respuesta ={"mensaje":"Ya existe un alumno con ese legajo"}
                codigoRespuesta = 400
            else:
                repo_alumnos.agregar(alumno_creado)
                respuesta ={"mensaje":"Alumno creado con exito"}
                codigoRespuesta = 201
        else:
            respuesta = {"mensaje":"faltan datos en el json"}
            codigoRespuesta = 400
    else:
        respuesta =  {"mensaje":"Los datos deben estar en formato json"}
        codigoRespuesta=400
    return jsonify(respuesta), codigoRespuesta


@bp_alumnos.route("/alumnos/<int:legajo>", methods =["PUT"])  
def modificar(legajo):
    if request.is_json:
        diccDatos = request.get_json()
        if  "nombre" in diccDatos and "apellido" in diccDatos:
            if repo_alumnos.existeAlumnoPorLegajo(legajo):
                repo_alumnos.modificarPorLegajo(legajo,diccDatos["apellido"],diccDatos["nombre"])
                respuesta ={"mensaje":"Alumno modficado"}
                codigoRespuesta = 200
            else:
                respuesta ={"mensaje":"Alumno no encontrado"}
                codigoRespuesta = 404
        else:
            respuesta = {"mensaje":"faltan datos en el json"}
            codigoRespuesta = 400
    else:
        respuesta =  {"mensaje":"Los datos deben estar en formato json"}
        codigoRespuesta=400
    return jsonify(respuesta), codigoRespuesta

@bp_alumnos.route("/alumnos/<int:legajo>", methods =["DELETE"])
def borrar(legajo):
    if repo_alumnos.existeAlumnoPorLegajo(legajo):
        repo_alumnos.eliminarPorLegajo(legajo)
        return jsonify({"mensaje":"Alumno eliminado"}), 200
    else:
        return jsonify({"mensaje":"Alumno no encontrado"}), 404