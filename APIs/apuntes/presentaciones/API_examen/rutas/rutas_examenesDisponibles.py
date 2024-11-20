from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoExamenesDisponibles

repo_examenes = obtenerRepoExamenesDisponibles()

bp_examenes = Blueprint("bp_examenes", __name__)

@bp_examenes.route("/examenesDisponibles/<int:idAlumno>", methods =["GET"])
def buscar_examen_alumno(idAlumno):
    examen_encontrado = repo_examenes.obtenerExamenPorIDAlumno(idAlumno)
    if examen_encontrado != None:
        return jsonify(examen_encontrado.toDiccionario()), 200
    else:
        return jsonify({"error":"no se encontró examen para el alumno indicado"}),404