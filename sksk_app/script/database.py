# from flask.cli import with_appcontext
from flask import Flask
from flask import Blueprint
from werkzeug.security import generate_password_hash
from datetime import datetime

from sksk_app import db
from sksk_app.models import User, Level
from sksk_app.utils.questions import QuestionManager

app = Flask(__name__)

qtdb = Blueprint('create', __name__)


# コマンド機能の作成
@qtdb.cli.command('all')
def create():
    db.create_all()
    print("Create All Tables ")

app.cli.add_command(create)

@qtdb.cli.command('init')
def init():
    level = 'ハン検5級'
    
    new_user = Level(
    level = level
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    name = 'test'
    email = 'test@test.com'
    password = '1234'
    regiestered_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_user = User(
    name = name,
    email = email,
    password = generate_password_hash(password, method='sha256'),
    registered_at = regiestered_at      
    )
    
    db.session.add(new_user)
    db.session.commit()

    db.session.add(new_user)
    db.session.commit()
    
    name = 'testE'
    email = 'testE@test.com'
    password = '1234'
    edit = 1
    regiestered_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_user = User(
    name = name,
    email = email,
    password = generate_password_hash(password, method='sha256'),
    edit = edit,
    registered_at = regiestered_at      
    )
    
    db.session.add(new_user)
    db.session.commit()


    print("Insert User Data ")

@qtdb.cli.command('delete_level')
def delete_level():
    QuestionManager.delete_testing_levels()

    print("Delete Levels")