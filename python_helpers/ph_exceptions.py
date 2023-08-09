class PhExceptions:
    def __init__(self, msg, function_name=None, line_num=None):
        self.msg = msg
        self.function_name = function_name
        self.line_num = line_num

    def get_details(self):
        if self.function_name:
            exception_msg = f'Exception Occurred at function: {self.function_name}, as: {self.msg}'
        else:
            exception_msg = f'Exception Occurred, as: {self.msg}'
        return exception_msg
