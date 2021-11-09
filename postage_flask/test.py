from postage import Flask_App
import unittest

class FlaskTestCase(unittest.TestCase):

    #Ensures that Flask was set up correctly, This test passes
    #def test_index(self):
        #tester = Flask_App.test_client(self)
        #response = tester.get('/', content_type='html/text')
        #self.assertEqual(response.status_code, 200)

    def test_1(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="150", Weight="120", LinearUnit="mm", 
        WeightUnit="grams", Width="100", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'150', response.data)

    def test_2(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="5", Weight="120", LinearUnit="inches", 
        WeightUnit="grams", Width="100", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'127', response.data)

    def test_3(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="5", Weight="120", LinearUnit="inches", 
        WeightUnit="grams", Width="100", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'120', response.data)

    def test_4(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="150", Weight="5", LinearUnit="mm", 
        WeightUnit="ounces", Width="100", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'141.75', response.data)

    def test_5(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="150", Weight="5", LinearUnit="mm", 
        WeightUnit="ounces", Width="100", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'100', response.data)

    def test_6(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="150", Weight="5", LinearUnit="mm", 
        WeightUnit="ounces", Width="7", WidthUnit="inches"),
        follow_redirects=True)
        self.assertIn(b'177.79999999999998', response.data)

    def test_7(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="160", Weight="20", LinearUnit="mm", 
        WeightUnit="grams", Width="120", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'True', response.data)

    def test_8(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="379", Weight="499", LinearUnit="mm", 
        WeightUnit="grams", Width="269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'False', response.data)                                


if __name__ == '__main__':
    unittest.main()