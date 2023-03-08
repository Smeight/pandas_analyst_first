import unittest
import pandas as pd
from io import StringIO
from contextlib import redirect_stdout
from main import calculate_statistics


class TestStatistics(unittest.TestCase):
    def setUp(self):
        data = {
            'product': ['pandas', 'numpy', 'plot'],
            'sales': [10120, 23422, 12412],
            'profit': [5123, 8120, 7221]
        }
        self.df = pd.DataFrame(data)

    def test_calculate_statistics(self):
        with StringIO() as buf, redirect_stdout(buf):
            calculate_statistics(self.df)
            output = buf.getvalue()
        self.assertEqual(output,
                         "Средний объем продаж в месяц: 15318.0\n"
                         "Самый популярный продукт: numpy\n"
                         "Продукт с самой высокой прибылью: numpy\n"
                         "Продукт с самой низкой прибылью: pandas")


if __name__ == '__main__':
    unittest.main()
