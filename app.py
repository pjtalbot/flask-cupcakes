"""Flask app for Cupcakes"""

from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake
from form import AddCupcakeForm

from flask_debugtoolbar import DebugToolbarExtension




app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():

    return render_template('base.html')

@app.route('/api/cupcakes')
def list_entires():

    form = AddCupcakeForm()

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=["POST"])
def new_cupcake():

    data = request.json

    cupcake = Cupcake(
        flavor = data['flavor'],
        size = data['size'],
        rating = data['rating'],
        image = data['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    return