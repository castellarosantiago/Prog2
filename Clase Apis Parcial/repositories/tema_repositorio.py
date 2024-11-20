from models import Tema
import random


temas_asignados = {}

def asignar_temas():
    for alumno_id in alumnos.keys():
        tema_id = random.choice(list(temas.keys()))
        temas_asignados[alumno_id] = tema_id

asignar_temas()

def get_tema_by_id(tema_id):
    return temas.get(tema_id)