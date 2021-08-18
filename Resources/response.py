"""This file houses general structure for a response
the class contains the status, data, and errors for a 
given request. """
import enum
import typing
import json
class ResponseStatus(enum):
        """An enum representation different status codes for a response"""
        OK = 200
        BAD_REQUEST = 400
        INTERNAL_SERVER_ERROR = 500

class Response:
        """Houses data errors and status code for handling an error response"""
        def __init__(self, status_code:ResponseStatus=None,data={}, errors=[]) -> None:
                self.__status = status_code
                self.__data = data
                self.__errors = errors

        def to_json(self):
                response = {}
                response["status"] = self.__status
                response["data"] = self.__data
                response["errors"] = self.__errors

        def set_status(self, status:ResponseStatus):
                """Sets the status code for the response"""
                self.__status = status

        def set_data(self, data:dict):
                """Sets the data for the response"""
                self.__data = data   

        def add_errors(self, error_msg:str):
                """adds an error to the list of errors"""
                self.__errors.append(error_msg)

        