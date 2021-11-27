class StatusCodeException(Exception):
    """The request status code is between 400 and 599"""

    def __init__(self, status_code):
        self.status_code = status_code
