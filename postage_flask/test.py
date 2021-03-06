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

    def test_9(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="160", Weight="20", LinearUnit="mm", 
        WeightUnit="grams", Width="120", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Postal rate: $0.49', response.data)   

    def test_10(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="160", Weight="35", LinearUnit="mm", 
        WeightUnit="grams", Width="120", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Postal rate: $0.8', response.data)

    def test_11(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="379", Weight="100", LinearUnit="mm", 
        WeightUnit="grams", Width="269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Postal rate: $0.98', response.data)

    def test_12(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="379", Weight="350", LinearUnit="mm", 
        WeightUnit="grams", Width="269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Postal rate: $2.4', response.data) 

    def test_13(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="37a9", Weight="35c0", LinearUnit="mm", 
        WeightUnit="grams", Width="2b69", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Non-numeric characters are not allowed for Length, Width, or Weight', response.data) 

    def test_14(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="-379", Weight="-350", LinearUnit="mm", 
        WeightUnit="grams", Width="-269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Negative inputs are not allowed', response.data)

    def test_15(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="379", Weight="501", LinearUnit="mm", 
        WeightUnit="grams", Width="269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Weight cannot be over 500g', response.data)        

    def test_16(self):
        tester = Flask_App.test_client(self)
        response = tester.post('/operation_result/', data=dict(Length="379", Weight="2", LinearUnit="mm", 
        WeightUnit="grams", Width="269", WidthUnit="mm"),
        follow_redirects=True)
        self.assertIn(b'Weight cannot be under 3g', response.data)                    


if __name__ == '__main__':
    unittest.main()