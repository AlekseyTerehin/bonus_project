class AbstractValidator:

    def __init__(self):
        self.queryset = None
        self.message_error = self.get_message_error()

    def is_valid(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    def get_message_error(self) -> str:
        raise NotImplementedError
