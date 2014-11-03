import unittest
import qj


class TestParseQueryStr(unittest.TestCase):
    def test_parse_1(self):
        res = qj.parse_query('a.b.c.d')
        self.assertEqual(['a', 'b', 'c', 'd'], res)

    def test_parse_2(self):
        res = qj.parse_query('a.b.c[10].d')
        self.assertEqual(['a', 'b', 'c', 10, 'd'], res)

    def test_parse_3(self):
        res = qj.parse_query('a.b.c[10][10]')
        self.assertEqual(['a', 'b', 'c', 10, 10], res)