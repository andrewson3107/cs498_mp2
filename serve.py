from flask import Flask, request
import socket, subprocess

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def serve():
    if request.method == 'GET':
        return socket.gethostname()
    elif request.method == "POST":
        subprocess.Popen(['python3', 'stress_cpu.py']) 
        return "Done"
        

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
