from flask import Blueprint, jsonify, request
import requests as r
from Config import Config

ai_api_bp = Blueprint('ai_api', __name__)

@ai_api_bp.route('/ai/', methods=['GET', 'POST'])
def frontend_routes():
    if request.method == "POST":
        return NotImplementedError
    else:
        return NotImplementedError

@ai_api_bp.route('/ai/info', methods=['POST'])
def ai_api_routes():
    data = request.get_json()
    return NotImplementedError