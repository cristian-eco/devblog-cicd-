import os

class Config:
    #Clave secreta para sesiones y formularios
    #En produccion debe ser variable de entorno
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    #configuracion para el modo debug
    #true = muestra errores detallados, recarga automatica
    #False = modo produccion, mas seguro

    DEBUG = os.environ.get('FLASK_DEBUG') or True

    #Puerto donde correra la aplicacion
    PORT = int(os.environ.get('PORT', 5000))

    #HOST - 0.0.0.0 permite conexiones externas (necesario para docker)
    HOST = os.environ.get('HOST', '0.0.0.0')