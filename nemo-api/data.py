class Data:
	__slots__ = ('raw')

	def __init__(self, raw: dict) -> None:
		self.raw = raw

	def __getattr__(self, item: str) -> 'Data':
		return Data(self.raw.get(item))

	def __str__(self) -> dict:
		return self.raw
