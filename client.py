import requests
import unittest
import time
        

class TestServerMethods(unittest.TestCase):

    def test_default(self):
        print(url)
        response=requests.get(url)
        self.assertEqual(response.status_code,200,"Error in the deafult endpoint, status code inst 200")
        self.assertGreater(len(response.text),1,'No message is being displayed')
        time.sleep(1)

    def test_file_creation(self):
        for file in ['d1','d2','d3']:
            response=requests.post(url+f'file_handler/{file}')
            self.assertEqual(response.status_code,200,"Error in the deafult endpoint, status code inst 200") 
            self.assertGreater(len(response.text),1,'The file content is not being returned')
            print(response.text)
            time.sleep(.2)

    def test_file_update(self):
        for file in ['d1','d2','d3']:
            response=requests.put(url+f'file_handler/{file}')
            self.assertEqual(response.status_code,200,"Error in the deafult endpoint, status code inst 200") 
            print(response.text)
            time.sleep(.2)


    def test_file_get(self):
        for file in ['d1','d2','d3']:
            response=requests.get(url+f'file_handler/{file}')
            self.assertEqual(response.status_code,200,"Error in the deafult endpoint, status code inst 200")
            self.assertGreater(len(response.text),1,'The file content is not being returned') 
            print(response.text) 
            time.sleep(0.2)
    
    def test_file_remotion(self):
        for file in ['d1','d2','d3']:
            response=requests.delete(url+f'file_handler/{file}')
            self.assertEqual(response.status_code,200,"Error in the deafult endpoint, status code inst 200")
            self.assertGreater(len(response.text),1,'The file content is not being returned') 
            time.sleep(.2)


if __name__=="__main__":
    url='http://127.0.0.1:5000/' # unittest does not provide an easy of adding a constructor to the testing class
    unittest.main()

