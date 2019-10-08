from flask import Flask, jsonify, request, render_template
from mongoconfig import connect
from flask_cors import CORS
from datetime import datetime
import pytz
import json

app = Flask(__name__)
CORS(app)

def getdate():
    ts_now = datetime.now(pytz.timezone('Asia/Kolkata'))
    ts_format = ts_now.strftime("%d-%m-%Y")
    return ts_format

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/getdata/<string:date>/<string:sensor>', methods=['GET'])
def getdata(date, sensor):
    client = connect()
    db = client['dripdata']
    # db = client['bqqldgp4wjjjjr2']
    col = db[date]
    records = list(col.find({}, {sensor:1, '_id':0}))
    return jsonify({'records': records})

@app.route('/getdata/<string:date>', methods=['GET'])
def getalldata(date):
    client = connect()
    db = client['dripdata']
    col = db[date]
    records = list(col.find({}, {'_id':0}))
    return jsonify({'records': records})

@app.route('/getdata/now', methods=['GET'])
def getdatanow():
    try:
        with open('static/current.json', 'r') as currentjson:
            current = json.load(currentjson)
        return jsonify(current)
    except Exception as e:
        print(e)
        return jsonify({"success": False})

@app.route('/deletedata/<string:date>', methods=['DELETE'])
def deletealldata(date):
    try:
        client = connect()
        db = client['dripdata']
        db[date].drop()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

@app.route('/setpump', methods=['POST'])
def setpump():
    try:
        pumpdata = request.get_json()
        print(pumpdata)
        client = connect()
        db = client['soif_settings']
        db['pump'].update_one({}, {'$set': {'settings': pumpdata}})
        print('Successfully updated setting!')
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

@app.route('/getpump', methods=['GET'])
def getpump():
    try:
        client = connect()
        db = client['soif_settings']
        col = db['pump']
        settings =  list(col.find({}, {'_id': 0}))
        return jsonify(settings[0])
    except Exception as e:
        print(e)
        return jsonify({'success': False})

@app.route('/insertdata', methods=['POST'])
def insertdata():
    sensordata = request.get_json()
    with open('static/current.json', 'w') as currentjson:
        json.dump(sensordata, currentjson)
    print(sensordata)
    mois_p0 = sensordata['moisture']['plant0']
    mois_p1 = sensordata['moisture']['plant1']
    temp = sensordata['temparature']
    humidity = sensordata['humidity']
    light = sensordata['light']
    client = connect()
    db = client['dripdata']
    dt = getdate()
    if dt in db.list_collection_names():
        db[dt].update_one({}, {"$push": { "moisture.plant0": mois_p0, "moisture.plant1": mois_p1, "temparature": temp, "humidity": humidity, "light": light}})
        print('Exists and added 1 entry')
        return jsonify({'success': True, 'firstEntryOfDay': False})
    else:
        db[dt].insert_one({"moisture": {"plant0": [], "plant1": []}, "temparature": [], "humidity": [], "light": [] })
        db[dt].update_one({}, {"$push": { "moisture.plant0": mois_p0, "moisture.plant1": mois_p1, "temparature": temp, "humidity": humidity, "light": light}})
        print('Created and added 1 entry')
        return jsonify({'success': True, 'firstEntryOfDay': True})