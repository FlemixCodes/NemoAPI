import typing

if typing.TYPE_CHECKING:
    from ...synchrone.api import NemoAPI
    from ....nemo_api.data import Data


class Utils:
    """
    Вспомогательные методы
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    def get_server_time(self) -> 'Data':
        """
        Получить время серверов Nemo
        """
        return self.__api.request("utils.getServerTime")
        
    def get_short_link(self, link: str) -> 'Data':
        """
        Сократить ссылку
        
        Параметры:
        link: str (ссылка)
        """
        params = {"link": link}
        return self.__api.request("utils.getShortLink", params)
    
    def get_stats(self) -> 'Data':
        """
        Получить статистику
        """
        return self.__api.request("utils.getStats")
