import unittest

from basket import Basket, Item


class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
        self.rice = Item("rice", 1.50)
        self.butter = Item("butter", 5.99)


    def test_add(self):
        self.assertEqual(self.basket.add(self.rice), {self.rice: 1})
        self.assertEqual(self.basket.add(self.rice, 2), {self.rice: 3})
        self.assertEqual(self.basket.add(self.butter, 2), {self.rice: 3, self.butter: 2})
        self.assertEqual(self.basket.add(self.butter, 3), {self.rice: 3, self.butter: 5})
        self.assertEqual(self.basket.add(self.rice, -1), "Can't add this amount of products")


    def test_delete(self):
        self.basket.add(self.rice, 6)
        self.basket.add(self.butter, 2)
        self.assertEqual(self.basket.delete(self.rice), {self.rice: 5, self.butter: 2})
        self.assertEqual(self.basket.delete(self.rice, 2), {self.rice: 3, self.butter: 2})
        self.assertEqual(self.basket.delete(self.butter), {self.rice: 3, self.butter: 1})
        self.assertEqual(self.basket.delete(self.rice, 3), {self.butter: 1})
        self.assertEqual(self.basket.delete(self.butter, 3), "Not enough products in basket")

        self.assertRaises(TypeError, self.basket.delete(self.rice, 3))


    def test_print_content(self):
        self.basket.add(self.rice, 6)
        self.basket.add(self.butter, 2)
        self.basket.add(self.butter, 1)
        self.basket.add(self.butter, -2)
        self.basket.print_content()


    def test_sum_price(self):
        self.basket.add(self.rice, 6)
        self.basket.add(self.butter, 2)
        self.basket.add(self.butter, 2)
        self.assertEqual(self.basket.sum_price(), 32.96)
        self.basket.delete(self.butter, 3)
        self.assertEqual(self.basket.sum_price(), 14.99)
        self.basket.add(self.butter, -2)
        self.assertEqual(self.basket.sum_price(), 14.99)


if __name__ == '__main__':
    unittest.main()
