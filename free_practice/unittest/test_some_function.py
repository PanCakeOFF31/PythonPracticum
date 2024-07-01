import unittest


class SomeFunctionTest(unittest.TestCase):
    def test_T0001_PS01_someFunction_ok(self):
        self.assertNotEqual(10, 15, 'not equals')

    def test_T0001_NS01_someFunction_exception(self):
        with self.assertRaises(TypeError):
            sum(1, 2)
