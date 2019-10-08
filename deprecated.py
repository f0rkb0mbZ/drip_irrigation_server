# @app.route('/setthreshold', methods=['POST'])
# def setpumpsetting():
#     try:
#         thresdata = request.get_json()
#         print(thresdata)
#         # config template
#         # con = {"pump0": 0.0, "pump1": 0.0}
#         with open('static/settings.json', 'w') as pumpcontrol:
#             # json.dump(thresdata, pumpcontrol)
#             pumpcontrol.write(json.dumps(thresdata))
#             pumpcontrol.close()
#         return jsonify({"success": True})
#     except Exception as e:
#         print(e)
#         return jsonify({"success": False})

# @app.route('/getthreshold', methods=['GET'])
# def getpumpsetting():
#     try:
#         with open('static/settings.json', 'r') as pumpdata:
#             pump = json.loads(pumpdata.read())
#             pumpdata.close()
#         print(pump)
#         return jsonify(pump)
#     except Exception as e:
#         print(e)
#         return jsonify({"success": False})
