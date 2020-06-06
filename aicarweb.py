from flask import Flask
from respberryController import RespberryController
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"
@app.route("/turn/<string:fx>")
def index(fx):    
    controller.control(fx)
    return "turn " + fx

if __name__ == '__main__':
    controller = RespberryController()
    app.run('0.0.0.0',1234)    