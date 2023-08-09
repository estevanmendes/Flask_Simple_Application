import requests
import unittest
import time
        

class TestServerMethods(unittest.TestCase):
    
    def check_status_code(self,response) -> None:
        self.assertEqual(200,response.status_code,"Error in the deafult endpoint, status code inst 200")
    
    def check_message_display(self,response) -> None:
        self.assertGreater(len(response.text),1,'No message is being displayed')

    def test_default(self) -> None:
        print(url)
        response=requests.get(url)
        self.check_status_code(response)
        self.check_message_display(response)
        time.sleep(1)

    def test_file_creation(self) -> None:
        for file in ['d1','d2','d3']:
            response=requests.post(url+f'file_handler/{file}')
            self.check_status_code(response)
            self.check_message_display(response)
            time.sleep(.2)

    def test_file_update(self) -> None:
        for file in ['d1','d2','d3']:
            response=requests.put(url+f'file_handler/{file}')
            self.check_status_code(response)
            self.check_message_display(response)
            time.sleep(.2)


    def test_file_get(self) -> None:
        for file in ['d1','d2','d3']:
            response=requests.get(url+f'file_handler/{file}')
            self.check_status_code(response)
            self.check_message_display(response)
            time.sleep(0.2)
    
    def test_file_remotion(self) -> None:
        for file in ['d1','d2','d3']:
            response=requests.delete(url+f'file_handler/{file}')
            self.check_status_code(response)
            self.check_message_display(response)
            self.assertIn(file,response.text,'The file was not removed') 
            time.sleep(.2)


if __name__=="__main__":
    url='http://127.0.0.1:5000/' # unittest does not provide an easy of adding a constructor to the testing class
    unittest.main()

