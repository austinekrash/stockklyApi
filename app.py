from flask import Flask, Blueprint
from flask_restplus import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv

from os import environ as env


import os
import logging.config
import settings
from api.restplus import api

from cache import cache
from mongo import mongoDB
# from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.contrib.fixers import ProxyFix

from api.products.endpoints.prices import ns as product_prices_namespace
from api.products.endpoints.pricesHistorical import ns as pricesHistorical_namespace
from api.products.endpoints.info import ns as product_info_namespace
from api.profile.endpoints.user import ns as profile_users_namespace
from api.wallet.endpoints.transactions import ns as wallet_transactions_namespace
from api.wallet.endpoints.holdings import ns as wallet_holdings_namespace
from api.products.endpoints.watchlist import ns as product_watchlist_namespace


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
MONGO_CONNECTION = env.get("MONGO_CONNECTION")
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config["MONGO_URI"] = MONGO_CONNECTION
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)
CORS(app, )
# api = Api(app)

# CORS(app, expose_headers='Authorization', supports_credentials=True)


def configure_app(flask_app):
    # flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config["MONGO_URI"] = MONGO_CONNECTION


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    # api.init_app(flask_app)
    api.init_app(blueprint)
    # app.register_blueprint(blueprint)
    api.add_namespace(wallet_holdings_namespace)
    api.add_namespace(wallet_transactions_namespace)
    api.add_namespace(product_info_namespace)
    api.add_namespace(product_prices_namespace)
    api.add_namespace(profile_users_namespace)
    api.add_namespace(product_watchlist_namespace)
    api.add_namespace(pricesHistorical_namespace)
    # api.add_namespace(wallet_balances_namespace)
    # api.add_namespace(product_sectors_namespace)

    # api.add_namespace(transactions_api)
    flask_app.register_blueprint(blueprint)

    # db.init_app(flask_app)
    mongoDB.init_app(app)


def main():
    log.info('Running')
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT,
            debug=settings.FLASK_DEBUG, threaded=True)


initialize_app(app)

if __name__ == "__main__":
    main()
