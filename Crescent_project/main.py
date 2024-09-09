from flask import Flask, Blueprint

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register)

if __name__ == '__main__':
    app.run(debug=True)