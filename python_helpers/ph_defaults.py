from python_helpers.ph_constants import PhConstants
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes


class PhDefaults:
    CHAR_ENCODING = PhConstants.CHAR_ENCODING_UTF8
    CHAR_ENCODING_ERRORS = PhConstants.CHAR_ENCODING_ERRORS_REPLACE
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    #############
    # Data Object
    #############
    # Common Objects
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    PRINT_INFO = True
    QUITE_MODE = False
    ENCODING = CHAR_ENCODING
    ENCODING_ERRORS = CHAR_ENCODING_ERRORS
