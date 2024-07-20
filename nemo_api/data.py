from typing import Any


class Data:
    """
    Удобная обёртка для работы со словарями
    
    Пример использования:
    data = Data({"name": "John", "surname": "Green"})\n
    print(data['name'], data.name)\n
    print(data['surname'], data.surname)
    """
    
    __slots__ = ('raw')

    def __init__(self, raw: Any) -> None:
        self.raw = raw
    
    def _process_data(self, item: Any) -> Any:
        if isinstance(self.raw, dict):
            data = self.raw.get(item)
        elif isinstance(self.raw, list) or isinstance(self.raw, tuple):
            data = self.raw[item]
        else:
            raise TypeError("Объект не является списком, кортежем или словарём")
        
        return data

    def __getattr__(self, item: Any) -> 'Data':
        data = self._process_data(item)
        return Data(data)

    def __getitem__(self, item: Any) -> 'Data':
        data = self._process_data(item)
        return Data(data)

    def __str__(self) -> str:
        return str(self.raw)
