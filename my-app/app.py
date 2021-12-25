from flask import Flask
import platform

app = Flask(__name__)

@app.route('/platform')
def get_platform():
    return platform.platform

@app.route('/system')
def get_system():
    return platform.system()

@app.route('/processor')
def get_processor():
    return platform.processor()

if __name__ == "__main__":
    app.run(debug=True)