import typing

if typing.TYPE_CHECKING:
    from ...asynchrone.api import NemoAPI
    from ...data import Data



class Database:
    """
    Методы базы данных
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    async def check(self, user_id: int) -> 'Data':
        """
        Проверить есть ли пользователь в базе данных
        
        Параметры:
        user_id: int (идентификатор пользователя)
        """
        params = {"user_id": user_id}
        return await self.__api.request("db.check", params)
