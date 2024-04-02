# 3rd parth dependencies
from waitress import serve
from flask import Flask
from deepface.api.src.modules.core.routes import blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app
deepface_app = create_app()

serve(deepface_app, host='0.0.0.0', port=5000, threads=2)