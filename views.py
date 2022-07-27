from flask import Blueprint

index = Blueprint("index")

@index.route("/")
def home():
    return "yes"