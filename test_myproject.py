import myproject
import unittest

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(myproject.hello_world(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
