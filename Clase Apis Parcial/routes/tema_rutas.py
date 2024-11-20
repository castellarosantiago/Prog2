from flask import Blueprint, jsonify, request
from repositories.tema_repository import get_tema_by_id, temas_asignados
from repositories.alumno_repository import get_alumno_by_legajo

examen_routes = Blueprint('examen_routes', __name__)

@examen_routes.route('/examenesDisponibles/<string:id_interno>', methods=['GET'])
def obtener_examen(id_interno):
    alumno = next((a for a in alumnos.values() if a.id_interno == id_interno), None)
    if alumno:
        tema_id = temas_asignados.get(alumno.legajo)