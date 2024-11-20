from flask import Blueprint, request, jsonify
from modelos.entidades.temaalumno import TemaAlumno
from modelos.repositorios.repositorios import obtenerRepoExamenesConfrmados

repo_confirmados = obtenerRepoExamenesConfrmados()

bp_examenesConfirmados = Blueprint("bp_examenesConfirmados", __name__)

@bp_examenesConfirmados.route("/examenesConfirmados", methods =["POST"])
def confirmar_examen():
    if request.is_json:
        diccDatos = request.get_json()
        if "alumno" in diccDatos and "tema" in diccDatos :
            examen_confirmado = TemaAlumno.fromDiccionario(diccDatos)
            
            if repo_confirmados.agregar(examen_confirmado):
                return jsonify({"mensaje":"Examen confirmado con éxito", "datos":examen_confirmado.toDiccionario()}), 201
            else:
                return jsonify({"error":"No se puedo cnfirmar el examen"}),400
            
        else:
            return jsonify({"error":"Faltan datos en el json, debe tener 'alumno' y 'tema'"}),400
    else:
        return jsonify({"error":"Debe enviar los datos en JSON"}),400