import unittest

from nemo_api import Data


class TestData(unittest.TestCase):
    def test_data(self):
        raw_dict = {"name": "John", "surname": "Green"}
        data = Data(raw_dict)
        
        print(data['name'], data['surname'])
        print(data.name, data.surname)
        
    def test_data_wrapped(self):
        raw_dict = {"name": "John", "surname": "Green", "other": {"weight": 87, "height": 170}}
        data = Data(raw_dict)
        
        print(data['other']['weight'])
        print(data['other']['height'])
        
    def test_data_exception(self):
        raw_dict = {"name": "John", "surname": "Green"}
        data = Data(raw_dict)
        
        with self.assertRaises(KeyError):
            print(data['name']['not_key'])
    
    def test_data_list(self):
        raw_dict = {"name": "John", "surname": "Green", "other": [{"weight": 90}, [0, 1, 2]]}
        data = Data(raw_dict)
        
        print(data['other'][0]['weight'])
        print(data['other'][1][0])
        
        print(data.other[0].weight)
        print(data.other[1][0])
        
        with self.assertRaises(IndexError):
            print(data['other'][13])
            
    def test_data_tuple(self):
        raw_dict = {"name": "John", "surname": "Green", "other": ({"weight": 90}, [0, 1, 2])}
        data = Data(raw_dict)
        
        print(data['other'][0]['weight'])
        print(data['other'][1][0])
        
        print(data.other[0].weight)
        print(data.other[1][0])
        
        with self.assertRaises(IndexError):
            print(data['other'][13])
    

if __name__ == "__main__":
    unittest.main()
