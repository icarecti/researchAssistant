from flask import Flask

from api.ingest_api import ingest_api
from api.visualization_api import visualization_api

app = Flask(__name__)
app.register_blueprint(ingest_api)
app.register_blueprint(visualization_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
