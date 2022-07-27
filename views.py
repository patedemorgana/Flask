from flask import Blueprint

index = Blueprint(__name__, "index")

@index.route("/")
def home():
    return "yes"

