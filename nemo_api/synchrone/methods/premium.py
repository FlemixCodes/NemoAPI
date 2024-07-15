import typing

if typing.TYPE_CHECKING:
    from ...synchrone.api import NemoAPI
    from ....nemo_api.data import Data


class Premium:
    """
    Премиум методы
    """
    
    __slots__ = ('__api')
    
    def __init__(self, api: 'NemoAPI') -> None:
        self.__api = api
        
    def quote(
        self, 
        name: str, 
        avatar: str, 
        text: str, 
        date: str, 
        background: str    
    ) -> bytes:
        """
        Сгенерировать цитату
        
        Параметры:
        name: str (имя пользователя)
        avatar: str (ссылка на аватарку пользователя)
        text: str (текст)
        date: str (дата)
        background (ссылка на фон)
        """
        params = {
            "name": name, 
            "avatar": avatar, 
            "text": text, 
            "date": date, 
            "background": background
        }
        
        return self.__api.request(
            "premium.citata", params, post=True, bytes=True
        )
