class NemoAPIError(Exception):
	__slots__ = ('error_code', 'error_msg')

	def __init__(self, error: dict) -> None:
		self.error_code = error['error_code']
		self.error_msg = error['error_msg']
