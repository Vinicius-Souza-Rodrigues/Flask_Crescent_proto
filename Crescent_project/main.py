from flask import Flask, Blueprint
from route.login import login
from route.register_admin import register_admin
from route.register_patro import register_patro
from route.register_user import register_user
from route.register_prop import register_prop

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register_user)
app.register_blueprint(register_prop)
app.register_blueprint(register_admin)
app.register_blueprint(register_patro)

if __name__ == '__main__':
    app.run(debug=True)