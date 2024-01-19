class NemoAPIError(Exception):
	def __init__(self, error: dict) -> None:
		self.error_code = error['error_code']
		self.error_msg = error['error_msg']
