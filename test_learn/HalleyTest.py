from calculator import Count
import unittest


class HalleyTestCase(unittest.TestCase):
    def setUp(self):
        print("["+self.__class__.__name__+"] "+"startup...")

    def tearDown(self):
        print("["+self.__class__.__name__+"] "+"teardown...")


class TestAdd(HalleyTestCase):
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)


class TestSub(HalleyTestCase):
    def test_sub(self):
        j = Count(5, 2)
        self.assertEqual(j.sub(), 3)

if __name__ == "__main__":
    unittest.main()
