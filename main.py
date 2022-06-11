from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    subprocess.call("sudo bash ./automation.sh", shell=True)
    return "worked"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)


    