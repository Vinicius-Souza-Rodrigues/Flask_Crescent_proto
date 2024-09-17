from flask import Flask
from route.login import login
from route.register_admin import register_admin
from route.register_patro import register_patro
from route.register_user import register_user
from route.register_prop import register_prop
from route.register_options import register_options
from route.forgot_password import forgot_password
from database import init_app, db  

app = Flask(__name__)

#app.secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/teste_crescent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

app.register_blueprint(login)
app.register_blueprint(register_user)
app.register_blueprint(register_prop)
app.register_blueprint(register_admin)
app.register_blueprint(register_patro)
app.register_blueprint(register_options)
app.register_blueprint(forgot_password)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
