import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, top_bid_price, top_ask_price, stock_price = getDataPoint(quote)
            self.assertEqual((stock, top_bid_price, top_ask_price, stock_price),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, top_bid_price, top_ask_price, stock_price = getDataPoint(quote)
            self.assertEqual((stock, top_bid_price, top_ask_price, stock_price),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio_priceBZero(self):
        price_a = 100
        price_b = 0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)

    def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 100
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, 0)

    def test_getRatio_normal(self):
        price_a = 100
        price_b = 50
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, 2)

    def test_getRatio_negativePrices(self):
        price_a = -100
        price_b = 50
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, -2)

    def test_getRatio_zeroPrices(self):
        price_a = 0
        price_b = 0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)


if __name__ == '__main__':
    unittest.main()
