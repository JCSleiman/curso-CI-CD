import unittest

class TestCICD(unittest.TestCase):

    def setUp(self):
      print("Inicio de las pruebas")

    def tearDown(self):
        print("Fin de las pruebas")

    def main(self):

        print("index funcional")
        self.assertEqual(render_template('index.html'))

if __name__ == '__main__':
    unittest.main()
