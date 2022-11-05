from abc import ABC, abstractmethod
import logging
class Service(ABC):
        def __init__(self) -> None:
                self.service_options = None
        def set_service_options(self, service_options) -> None:
                self.service_options = service_options
                self.service_output = None

        
        @abstractmethod
        def process_request(self):
                pass

        def handle_request(self):
                try:
                        return self.process_request()
                except Exception as e:
                        logging.error(e)
                        raise Exception(e)