import unittest

from nemo_api import Data, NemoBaseError, NemoAPIError
from nemo_api.synchrone import NemoAPI


class TestSynchrone(unittest.TestCase):
    def test_request(self):
        api = NemoAPI("nemo.t.test")
        response = api.request("utils.getServerTime")
        self.assertTrue(isinstance(response, Data))
        
    def test_request_exception(self):
        api = NemoAPI("nemo.t.test")
        
        with self.assertRaises(NemoAPIError):
            api.request("nomethod")
            
    def test_request_base_exception(self):
        api = NemoAPI("nemo.t.test")
        
        with self.assertRaises(NemoBaseError):
            api.request("nomethod")  

if __name__ == "__main__":
    unittest.main()
