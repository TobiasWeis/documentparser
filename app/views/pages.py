import os
import app
from flask import Blueprint, redirect, flash, url_for
from werkzeug.utils import secure_filename
from flask import request, render_template, make_response, jsonify, abort
from app.DocumentParser.DocumentParser import *

pages_blueprint = Blueprint('pages_blueprint', __name__, url_prefix="", template_folder='../templates/', static_folder='static', static_url_path='../static/')


@pages_blueprint.route('/', methods=['GET'])
def login():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['pdf', 'jpg', 'jpeg', 'png']


@pages_blueprint.route('/process', methods=['GET', 'POST'])
def processInputFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            abort(400)

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            abort(400)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/tmp/', filename))

            docparse = DocumentParser()
            pages = docparse.process(os.path.join('/tmp/', filename))

            data = {'message': 'Success',
                    'pages': pages.get_serializable_json()}
            return make_response(jsonify(data), 200)
        else:
            abort(400)
