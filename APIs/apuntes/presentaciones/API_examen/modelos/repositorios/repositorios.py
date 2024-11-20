from modelos.repositorios.repositorioAlumnos import RepositorioAlumno
from modelos.repositorios.repositorio_tema import RepositorioTema
from modelos.repositorios.repositorio_examenes import RepositorioExamenes
from modelos.repositorios.repositorio_examenesConfirmados import RepositorioExamenesConfirmados

repo_alumnos = None
repo_temas = None
repo_examenes = None
repo_confirmados =None

def obtenerRepoAlumnos()-> RepositorioAlumno:
    global repo_alumnos
    if not isinstance(repo_alumnos, RepositorioAlumno):
        repo_alumnos = RepositorioAlumno()
    return repo_alumnos

def obtenerRepoTemas()-> RepositorioTema:
    global repo_temas
    if not isinstance(repo_temas, RepositorioTema):
        repo_temas = RepositorioTema()
    return repo_temas

def obtenerRepoExamenesDisponibles()-> RepositorioExamenes:
    global repo_examenes
    if not isinstance(repo_examenes, RepositorioExamenes):
        repo_examenes = RepositorioExamenes()
    return repo_examenes

def obtenerRepoExamenesConfrmados()-> RepositorioExamenesConfirmados:
    global repo_confirmados
    if not isinstance(repo_confirmados, RepositorioExamenesConfirmados):
        repo_confirmados = RepositorioExamenesConfirmados()
    return repo_confirmados