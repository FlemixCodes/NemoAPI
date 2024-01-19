class NemoAPIError(Exception):
	__slots__ = ('error', 'error_code', 'error_msg')

	def __init__(self, error: dict) -> None:
		self.error = error
		self.error_code = self.error['error_code']
		self.error_msg = self.error['error_msg']

	def __str__(self):
		return f"({self.error_code}) {self.error_msg}"
