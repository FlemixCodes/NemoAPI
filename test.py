from nemo_api import NemoAPI

api = NemoAPI(token="nemo.t.token", version="1")
info = api.acc_get_info()
print(info)