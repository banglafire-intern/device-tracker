from flask import Flask
from flask import jsonify
from who_is_on_my_wifi import *

app = Flask(__name__)

@app.route('/app-status')
def app_status():
  return "Success"

@app.route('/get-device-list')
def get_device():
  WHO = who()
  deviceList=[]
  for i in range(0, len(WHO)):
    deviceList.append(WHO[i])
    #print(WHO[i])
  return jsonify(deviceList)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)