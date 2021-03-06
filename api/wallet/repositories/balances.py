
from api import auth
from mongo import mongoDB
# from database.db import get_db

# from stockklyApi.api.wallet.business import prices

from bson import json_util


def get_balance(userId, ticker):
    queryresult = mongoDB.db.balances.find_one({"userId": userId, "ticker": ticker})
    return(queryresult)


def get_balances(userId):
    return mongoDB.db.balances.find({"userId": userId})


def create_balance(userEmail, data):
    balance = {
        'ticker': data['ticker'],
        'userId': userEmail,
        'qty': data['qty']
    }
    return mongoDB.db.balances.insert_one(balance)


def update_balance(userEmail, ticker, qty):
    return mongoDB.db.balances.update_one({'ticker': ticker, "userId": userEmail}, {"$set": {"qty": qty}}, upsert=True)
