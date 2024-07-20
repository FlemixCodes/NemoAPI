import requests

from ..data import Data
from ..exceptions import NemoAPIError, NemoResponseError
from .methods import Account, Chats, Database, Premium, Utils


class NemoAPI:
    """
    Обёртка для API чат менеджера Nemo (vk.com/nemocm)
    """
    
    __slots__ = (
        '__access_token', 
        '__version', 
        '__base_params',
        'acc',
        'chats',
        'db',
        'premium',
        'utils'
    )
    
    base_url = "https://api.nemo-bot.ru/m/"

    def __init__(self, access_token: str, version: str = "1") -> None:
        self.__access_token = access_token
        self.__version = version
        self.__base_params = f"?v={self.__version}&access_token={self.__access_token}"
        
        self.acc = Account(self)
        self.chats = Chats(self)
        self.db = Database(self)
        self.premium = Premium(self)
        self.utils = Utils(self)

    def request(
        self, 
        method: str, 
        params: dict | None = None, 
        post: bool = False,
        bytes: bool = False
    ) -> Data | bytes:
        """
        Выполнить метод API
        
        method: str (метод)
        params: dict (параметры)
        post: bool (если True, выполняется post запрос, иначе get)
        bytes: bool (если True, возвращаются байты)
        """
        
        if post:
            response = requests.post(
                f"{self.base_url}{method}{self.__base_params}", params
            )
        else:
            response = requests.get(
                f"{self.base_url}{method}{self.__base_params}", params
            )

        if response.status_code != 200:
            raise NemoResponseError("Апи не вернуло правильный ответ")
        
        data = response.json()
        if data.get("error"):
            raise NemoAPIError(data['error'])
        
        if bytes:
            return response.content
        
        return Data(data)
