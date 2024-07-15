import typing

if typing.TYPE_CHECKING:
    from ...asynchrone.api import NemoAPI
    from ...data import Data



class Utils:
    """
    Вспомогательные методы
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    async def get_server_time(self) -> 'Data':
        """
        Получить время серверов Nemo
        """
        return await self.__api.request("utils.getServerTime")
        
    async def get_short_link(self, link: str) -> 'Data':
        """
        Сократить ссылку
        
        Параметры:
        link: str (ссылка)
        """
        params = {"link": link}
        return await self.__api.request("utils.getShortLink", params)
    
    async def get_stats(self) -> 'Data':
        """
        Получить статистику
        """
        return await self.__api.request("utils.getStats")
