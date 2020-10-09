from flask import Blueprint, jsonify, request
import requests as r

from Config import Config

scraper_ip = Config.SCRAPER_IP
scraper_port=Config.SCRAPER_PORT

frontend_ip=Config.FRONTEND_IP
frontend_port=Config.FRONTEND_PORT

scraper_api_bp = Blueprint('scraper_api', __name__)

@scraper_api_bp.route('/scraper/<region>', methods=['GET', 'POST'])
def frontend_routes(region=None):
    if request.method == "POST":
        data = request.get_json()
        r.post()
        return NotImplementedError
    else:
        if region is None:
            return jsonify(message="No region has been provided"), 204
        response = r.get('{ip}:{port}/scrape/{}'.format(scraper_ip,scraper_port,region))
        return jsonify(message=response.text), response.status_code

@scraper_api_bp.route('/scraper/info', methods=['POST'])
def scraper_api_routes():
    data = request.get_json()
    return NotImplementedError