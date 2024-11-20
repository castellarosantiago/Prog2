from flask import Blueprint, jsonify
from repositories.alumno_repository import get_alumno_by_legajo

alumno_routes = Blueprint('alumno_routes', __name__)

@alumno_routes.route('/alumnos/<int:num_legajo>', methods=['GET'])
def obtener_alumno(num_legajo):
    alumno = get_alumno_by_legajo(num_legajo)
    if alumno:
        return jsonify({"legajo": alumno.legajo, "IDinterno": alumno.id_interno, "nombre": alumno.nombre, "apellido": alumno.apellido}), 200
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404