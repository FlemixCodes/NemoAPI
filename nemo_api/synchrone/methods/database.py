import typing

if typing.TYPE_CHECKING:
    from ...synchrone.api import NemoAPI
    from ....nemo_api.data import Data


class Database:
    """
    Методы базы данных
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    def check(self, user_id: int) -> 'Data':
        """
        Проверить есть ли пользователь в базе данных
        
        Параметры:
        user_id: int (идентификатор пользователя)
        """
        params = {"user_id": user_id}
        return self.__api.request("db.check", params)
