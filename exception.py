class BusinessException(Exception):
    pass


class ReadingException(BusinessException):
    message = 'I have no idea what you are talking about'


class UnknownResource(BusinessException):
    message = 'I\'ve never seen this {0} stuff.'

    def __init__(self, resource):
        self.message = self.message.format(resource)
