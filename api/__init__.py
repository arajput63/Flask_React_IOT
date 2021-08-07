import os
from flask import Flask, render_template, request
from flask.helpers import send_from_directory

import json
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(
        __name__, 
        instance_relative_config=True,
        static_url_path="",
        static_folder="../react-frontend/build"
    ) #for using react-frontend

    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'test.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple api response that says hello for testing comms with backend server
    @app.route('/hello', methods=('GET', 'POST'))
    def hello():
        print(request.get_json())
        print("Hello API has been called!")
        #flask.jsonify() vs json.dumps() for correct headers in response object? investigate more later...
        return json.dumps({'message': 'Hello, From flask'})

    @app.route('/')
    def index():
        # return render_template("index.html")
        return send_from_directory(app.static_folder, 'index.html') #for using react frontend

    from . import db
    db.init_app(app) # from a terminal, run 'flask init-db' to recreate database in instance folder

    from . import routes
    app.register_blueprint(routes.bp)

    return app
