"""The base class for all resources in this project"""
from Flask import request
from abc import ABC, abstractmethod
from response import ResponseStatus, Response

class Resource(ABC):
        """The purpose of this class is to house the structure of resources
        that are to be used in the app file. Each resource should have  a request object in it"""
        def __init__(self, request:request) -> None:
            self.request = request
            self.response = None

        @abstractmethod
        def process(self) -> Response:
                pass
                
                