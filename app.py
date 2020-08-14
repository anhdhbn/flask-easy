from flask import Flask, jsonify
from models import init_app, db
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_app(app)

@app.route("/")
def index():
    return "Hello"

@app.route('/example/all', methods=['GET'])
def get_all_data():
    all_data = models.ExampleData.query.all()
    return jsonify(models.ExampleData.serialize_list(all_data))

from app import app, db
import click


@app.cli.command("createall")
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.echo('Dropped database.')
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')