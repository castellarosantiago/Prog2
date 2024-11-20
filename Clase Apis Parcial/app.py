from flask import Flask
from routes.alumno_routes import alumno_routes
from routes.examen_routes import examen_routes

app = Flask(__name__)

# Registrar las rutas
app.register_blueprint(alumno_routes)
app.register_blueprint(examen_routes)
##inicializacion del repo
if __name__ == '__main__':
    app.run(debug=True)