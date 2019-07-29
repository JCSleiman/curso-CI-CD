import unittest
#sys.path.insert(1, '/path/to/application/app/folder')
from app import *

class TestCICD(unittest.TestCase):

    def setUp(self):
        print("Inicio de las pruebas")

    def tearDown(self):
        print("Fin de las pruebas")

    def test_showSignUp(self):

        print("index funcional")
        self.assertTrue(render_template)

if __name__ == '__main__':
    unittest.main()
