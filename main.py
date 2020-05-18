from flask import Flask
from flask import request,jsonify,Response
import json

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)




app = Flask(__name__)

def get_json(headers,method,path,body):
    d={
        "path" : path,
        "headers" : {},
        "method" : method,
        "body" : body.decode("UTF8")
    }  
    for i in headers:
        key, val = i
        d["headers"][key]=val
    resp = json.dumps(d,indent=4)
    print(resp)
    return resp




@app.route('/', defaults={'path': ''},methods=["POST","GET","OPTIONS","PUT","DELETE"])
@app.route('/<path:path>',methods=["POST","GET","OPTIONS","PUT","DELETE"])
def catch_all(path):
    return Response(get_json(request.headers,request.method,request.full_path,request.data),mimetype='application/json')
   

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)