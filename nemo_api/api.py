import requests

from .data import Data
from .exceptions import NemoAPIError


class NemoAPI:
    __slots__ = ('__access_token', '__version')

    def __init__(self, access_token: str, version: str) -> None:
        self.__access_token = access_token
        self.__version = version

    def request(self, method: str, params: dict = {}) -> 'Data':
        response = requests.get(f"https://api.nemo-bot.ru/m/{method}", params)
        if response.status_code == 200:
            data = response.json()
            if not data.get("error"):
                return Data(data)
            else:
                raise NemoAPIError(data['error'])

    def acc_get_info(self):
        params = {
            "access_token": self.__access_token,
            "v": self.__version
        }
        response = self.request("acc.getInfo", params)
        return response

    def chats_get_members(self, chat_id: int):
        ...

    def chats_get_by_id(self, chat_id: int):
        ...

    def chats_edit_title(self):
        ...

    def chats_ban(self):
        ...

    def chats_mute(self):
        ...

    def chats_unban(self):
        ...

    def chats_unmute(self):
        ...

    def utils_get_server_time(self):
        ...

    def utils_get_short_link(self):
        ...

    def utils_get_stats(self):
        ...

    def db_check(self):
        ...
