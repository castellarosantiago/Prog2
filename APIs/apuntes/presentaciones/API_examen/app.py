from flask import Flask
from rutas.rutas_alumnos import bp_alumnos
from rutas.rutas_temas import bp_temas
from rutas.rutas_examenesDisponibles import bp_examenes
from rutas.ruta_examenesConfirmados import bp_examenesConfirmados
app = Flask(__name__)

app.register_blueprint(bp_alumnos)
app.register_blueprint(bp_temas)
app.register_blueprint(bp_examenes)
app.register_blueprint(bp_examenesConfirmados)

if __name__=="__main__":
    app.run(debug=True)



    