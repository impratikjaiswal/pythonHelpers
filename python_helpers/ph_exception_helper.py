from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil


class PhExceptionHelper:
    def __init__(self, msg=None, function_name=None, line_num=None, exception=None):
        self.msg = msg
        self.function_name = function_name
        self.line_num = line_num
        self.exception = exception
        self.exception_str = str(self.exception) if self.exception else None

    def get_exception(self):
        return self.exception(self.msg)

    def get_details(self):
        exception_details = PhUtil.get_key_value_pair('Detail(s) are', PhConstants.SEPERATOR_TWO_LINES.join(
            filter(None, [self.exception_str, self.msg])))
        exception_msg = PhUtil.get_key_value_pair(PhConstants.EXCEPTION_OCCURRED_AT_FUNC,
                                                  self.function_name) if self.function_name else PhConstants.EXCEPTION_OCCURRED
        return PhConstants.SEPERATOR_MULTI_OBJ.join([exception_msg, exception_details])
