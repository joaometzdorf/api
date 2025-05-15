from flask import Flask
from flask_cors import CORS
from auth import login
import posts

app = Flask(__name__)
CORS(app)

app.route("/login", methods=["POST"])(login)

app.route("/posts", methods=["GET"])(posts.get_posts)
app.route("/posts", methods=["POST"])(posts.create_post)
app.route("/posts/<id>", methods=["PATCH"])(posts.update_post)
app.route("/posts/<id>", methods=["DELETE"])(posts.delete_post)
