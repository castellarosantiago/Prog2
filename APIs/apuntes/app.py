##importar libreria de servidores flask
from flask import Flask

## inicializar el sv Flask

app = Flask(__name__)
if __name__=="__main__":
        app.run(debug=True)

@app.route("/")
def main():
        return("Saracatunga")