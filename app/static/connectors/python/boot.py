from flask import Flask

from connectors.python import filemanager

app = Flask(__name__)

@app.route(filemanager.base_url)
def dispatch():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()