import typing

if typing.TYPE_CHECKING:
    from ...asynchrone.api import NemoAPI
    from ...data import Data



class Chats:
    """
    Методы чатов
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    async def edit_title(self, chat_id: str, title: str) -> 'Data':
        """
        Изменить название чата
        
        Параметры:
        chat_id: str (идентификатор чата Nemo)
        title: str (название чата)
        """
        params = {"chat_id": chat_id, "title": title}
        return await self.__api.request("chats.editTitle", params)
