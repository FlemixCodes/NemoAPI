from nemo_api import NemoAPI

api = NemoAPI(access_token="nemo.t.test", version="1")
info = api.acc_get_info()
print(info)