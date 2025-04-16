import unittest
from app import Hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        # Test the Hello_world function
        self.assertEqual(Hello_world(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
    