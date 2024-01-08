from flask import Flask

#def create_app():
#    app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')
#    app.config['DEBUG'] = False
#    return app

app = Flask(__name__, static_folder='static', static_url_path='/static',template_folder='templates')
#Set a secret key for session management
app.secret_key = 'wme2023'


#app.config['DEBUG'] = False
from app import views




