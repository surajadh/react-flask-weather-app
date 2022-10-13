from flask import Flask, request
from .service_layer.service import Service
from .service_layer.service_impl import ServiceImpl

app = Flask(__name__)

@app.route('/forecast')
def get_current_weather():
    zip = request.args.get('zip')
    if not zip:
        return 'zip needs to be provided', 400

    for c in zip:
        if c not in '0123456789':
            return 'not valid zip', 400
            
    service : Service = ServiceImpl()
    return service.get_min_max(zip)
