from flask import Blueprint, redirect, render_template

api_views = Blueprint('api_views', __name__, template_folder='../templates')

#API Documentation
@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')