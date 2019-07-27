
class RsException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RsUserWarning(RsException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Fetch500Error(RsException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Fetch400Error(RsUserWarning):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UnknownNon200Error(RsException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
