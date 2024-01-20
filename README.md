# NemoAPI
### Использование
```python
from nemo_api import NemoAPI

api = NemoAPI(access_token="ваш токен", version="1")
info = api.acc_get_info() # Все методы сделаны под стиль Python (acc.getInfo -> acc_get_info)
print(info.response) # Обращение к данным происходит через точку, но вы также можете сделать info.raw['response']
```
