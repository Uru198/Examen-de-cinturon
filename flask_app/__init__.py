#INICIALIZA la aplicación
from flask import Flask

app = Flask(__name__)

#Establecemos una secret key
app.secret_key = "una llave secreta"
