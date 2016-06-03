from flask import Flask

app = Flask(__name__)
app.config.from_envvar('config', silent=True)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
if __name__ == '__main__':
    #   app.run(debug = True)
    app.debug = True
    app.run()
