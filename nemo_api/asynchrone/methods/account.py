import typing

if typing.TYPE_CHECKING:
    from ...asynchrone.api import NemoAPI
    from ...data import Data


class Account:
    """
    Методы аккаунта
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    async def get_info(self) -> 'Data':
        """
        Получить информацию об аккаунте
        """
        return await self.__api.request("acc.getInfo")
    
    async def check_premium(self) -> 'Data':
        """
        Получить информацию о премиум доступе аккаунта
        """
        return await self.__api.request("acc.checkPremium")
