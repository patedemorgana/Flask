from flask import Flask
from views import index


app = Flask(__name__)
app.register_blueprint(index, url_prefix="/home")

if __name__ == '__main__':
    app.run(debug=True, port=8080)