from flask_restplus import fields
from stockklyApi.api.restplus import api


company = api.model('Company', {
    'name': fields.String,
    'url': fields.String,
}
)

quote = api.model('Quote', {
    'symbol': fields.String,
    'currency': fields.String,
}
)

product = api.model('Product', {
    'ticker': fields.String,
    'displayTicker': fields.String,
    'name': fields.String,
    'description': fields.String,
    'company': fields.Nested(company),
    'sector': fields.String,
    'quote':  fields.Nested(quote),
    # "exchanges": ["CPRO"],
})


price = api.model('Price', {
    'ticker': fields.String,
    'open': fields.Float,
    'change': fields.Float,
    'price':  fields.Float,
    'movement':  fields.Float
})