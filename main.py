from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def hello():
    os.system("sudo docker-compose -f /home/pi/docker/docker-compose.yml pull")
    os.system("sudo docker-compose -f /home/pi/docker/docker-compose.yml up --detach")
    os.system("sudo docker image prune -f")
    return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)


    