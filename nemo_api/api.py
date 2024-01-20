import requests

from .data import Data
from .exceptions import NemoAPIError, ResponseError


class NemoAPI:
    __slots__ = ('__access_token', '__version', 'base_params')

    def __init__(self, access_token: str, version: str) -> None:
        self.__access_token = access_token
        self.__version = version
        self.base_params = f"?v={self.__version}&access_token={self.__access_token}"

    def request(self, method: str, params: dict | None = None) -> 'Data':
        response = requests.get(
            f"https://api.nemo-bot.ru/m/{method}{self.base_params}", 
            params
        )

        if response.status_code == 200:
            data = response.json()
            if not data.get("error"):
                return Data(data)
            else:
                raise NemoAPIError(data['error'])
        else:
            raise ResponseError("Api returned a code other than 200")

    def acc_get_info(self):
        return self.request("acc.getInfo")

    def chats_get_members(self, chat_id: int):
        params = {"chatId": chat_id}
        return self.request("chats.getMembers", params)

    def chats_get_by_id(self, chat_id: int):
        params = {"chatId": chat_id}
        return self.request("chats.getById", params)

    def chats_edit_title(self, chat_id: int):
        params = {"chatId": chat_id}
        return self.request("chats.editTitle", params)

    def chats_ban(
        self, chat_id: int, user_id: int | str, 
        time: int = 0, reason: str = None
    ):
        params = {
            "chatId": chat_id, 
            "userId": user_id,
            "time": time,
            "reason": reason
        }

        return self.request("chats.ban", params)

    def chats_mute(
        self, chat_id: int, user_id: int | str, 
        time: int = 0, reason: str = None
    ):
        params = {
            "chatId": chat_id, 
            "userId": user_id,
            "time": time,
            "reason": reason
        }

        return self.request("chats.mute", params)

    def chats_unban(self, chat_id: int, user_id: int | str):
        params = {"chatId": chat_id, "userId": user_id}
        return self.request("chats.unban", params)

    def chats_unmute(self, chat_id: int, user_id: int | str):
        params = {"chatId": chat_id, "userId": user_id}
        return self.request("chats.unmute", params)

    def utils_get_server_time(self):
        return self.request("utils.getServerTime")

    def utils_get_short_link(self, url: str):
        params = {"url": url}
        return self.request("utils.getShortLink", params)

    def utils_get_stats(self):
        return self.request("utils.getStats")

    def db_check(self, user_id: int | str):
        params = {"user_id": user_id}
        return self.request("db.check", params)
