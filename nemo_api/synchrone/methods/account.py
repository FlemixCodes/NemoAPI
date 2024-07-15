import typing

if typing.TYPE_CHECKING:
    from ...synchrone.api import NemoAPI
    from ....nemo_api.data import Data


class Account:
    """
    Методы аккаунта
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    def get_info(self) -> 'Data':
        """
        Получить информацию об аккаунте
        """
        return self.__api.request("acc.getInfo")
