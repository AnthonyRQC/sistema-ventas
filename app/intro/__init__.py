from flask import Blueprint

# creando el blueprint intro de la pagina
intro_bp = Blueprint('intro_bp', __name__,
                     static_folder="static",
                     static_url_path="/intro/static",
                     template_folder="templates"
                     )


from app.intro import intro
