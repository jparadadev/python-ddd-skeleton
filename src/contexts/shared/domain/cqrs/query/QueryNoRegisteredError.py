from src.contexts.shared.domain.DomainError import DomainError


class QueryNotRegisteredError(DomainError):

    ERROR_ID = 'dfecfc84-d4a3-4e5e-be5d-c6e5cf9824c1'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Query not registered.'
        self.message = msg

    def to_primitives(self) -> dict | list:
        return {
            'message': self.message,
            'id': self.get_id(),
        }

    def get_id(self) -> str:
        return QueryNotRegisteredError.ERROR_ID
