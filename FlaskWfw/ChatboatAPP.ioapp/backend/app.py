from flask import Flask,request,jsonify
from flask_socketio import SocketIO,emit
# for react js
from flask_cors import CORS

app=Flask(__name__)
app.config['SECRET_KEY']="secret"
CORS(app,resources={r"/":{"origins":"*"}})
SocketIO=SocketIO(app,cors_allowed_origins="*")

# route 
@app.route('/http-call')
def http_call():
    data={'data':"This text was fetching"}
    return jsonify(data)

# for connect client side
@SocketIO.on('connected')
def connected():
    print(request.sid)
    print("Clienr is connected")
    # send data to client side by emit
    emit("connect",{
        "data":f"id:{request.sid} is connected"
    })

@SocketIO.on('disconnect')
def disconnected():
    print("User disconnected")
    # broadcast it means everyone is disconnect from chat when true
    emit("disconnect",f"user {request.sid} has been disconnected",broadcast=True)

# handle data from frontend
@SocketIO.on('data')
def handle_message(data):
    print("data from the front end :",str(data))
    emit("data",{
        'data':data,"id":request.sid
    },broadcast=True)

    
# start flask application
if __name__=='__main__':
    SocketIO.run(app,debug=True,port=5001)