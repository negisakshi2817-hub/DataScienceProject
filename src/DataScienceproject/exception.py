import sys
from src.DataScienceproject.logger import logging

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message, error_detail)

    def __str__(self):
        return self.error_message

    def get_detailed_error_message(error_message: Exception, error_detail: sys.exc_info()) -> str:
         _, _, exc_tb = error_detail
         file_name = exc_tb.tb_frame.f_code.co_filename
         error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error_message)}]"
         return error_message
   

