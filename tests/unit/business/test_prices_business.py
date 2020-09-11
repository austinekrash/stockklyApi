from api.products.business.prices import get_price
from unittest.mock import patch


@patch("api.products.business.prices.get_product")
@patch("api.products.business.prices.get_price_latest")
def test_something(mock_get_price_latest, mock_get_product):
  dummy_price = {
    'price': 12.34,
    'symbol': 'BTC:USD',
  }

  dummy_product = {
    'quote': {
      'symbol': 'BTC:USD'
    },
    'displayTicker':'BTC'
  }
  mock_get_price_latest.return_value = dummy_price
  mock_get_product.return_value = dummy_product

  resval = get_price('BTC:USD')
  assert resval.get('price') == 12.34