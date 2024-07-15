import unittest

from nemo_api import Data, NemoBaseError, NemoAPIError
from nemo_api.asynchrone import NemoAPI


class TestAsynchrone(unittest.IsolatedAsyncioTestCase):
    async def test_request(self):
        api = NemoAPI("nemo.t.test")
        response = await api.request("utils.getServerTime")
        self.assertTrue(isinstance(response, Data))
        
    async def test_request_exception(self):
        api = NemoAPI("nemo.t.test")
        
        with self.assertRaises(NemoAPIError):
            await api.request("nomethod")
            
    async def test_request_base_exception(self):
        api = NemoAPI("nemo.t.test")
        
        with self.assertRaises(NemoBaseError):
            await api.request("nomethod")  

if __name__ == "__main__":
    unittest.main()
