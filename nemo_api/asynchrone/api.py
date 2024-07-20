import asyncio

import aiohttp

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
        
    async def _request_get(
        self, url: str, params: dict | None, bytes: bool = False
    ) -> dict | bytes:
        """
        Выполнить GET запрос
        
        url: str (ссылка)
        params: dict (параметры)
        bytes: bool (если True, возвращаются байты)
        """
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=params) as response:
                if response.status != 200:
                    raise NemoResponseError("Апи не вернуло правильный ответ")
                
                if bytes:
                    return await response.content.read()
                return await response.json()
        
    async def _request_post(
        self, url: str, params: dict | None, bytes: bool = False
    ) -> dict | bytes:
        """
        Выполнить POST запрос
        
        url: str (ссылка)
        params: dict (параметры)
        bytes: bool (если True, возвращаются байты)
        """
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=params) as response:
                if response.status != 200:
                    raise NemoResponseError("Апи не вернуло правильный ответ")
                
                if bytes:
                    return await response.content.read()
                return await response.json()

    async def request(
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
        
        url = f"{self.base_url}{method}{self.__base_params}"
        
        if post:
            data = await self._request_post(url, params, bytes)
        else:
            data = await self._request_get(url, params, bytes)
        
        # Задержка, чтоб все соединения aiohttp успели закрыться и не было варнингов
        await asyncio.sleep(0.330)
        
        if data.get("error"):
            raise NemoAPIError(data['error'])
        
        if bytes:
            return data
        
        return Data(data)
