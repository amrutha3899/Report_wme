from flask import Flask, render_template, request, redirect, url_for, send_from_directory,flash
from flask import send_file
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import make_response
import ast
import json
import sys
import pandas as pd
import pyodbc
import script_upd
from app import app

from datetime import datetime
current_time = datetime.now()

if __name__ == '__main__':
    app.run(debug=True) # removed debug=True
#   app.run(debug=True, port=8080)

# if __name__ == '__main__':
#     # Use Waitress for serving the app
#     app = create_app()
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)


