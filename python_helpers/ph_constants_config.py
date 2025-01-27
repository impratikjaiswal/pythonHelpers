from ._git_info import GIT_SUMMARY
from ._tool_name import TOOL_NAME
from ._version import __version__


class PhConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'Python Helpers'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_DESCRIPTION = f'A Python software package suite to provide various utility functions.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, Common Functions, Funcs, Util, Utility'
    TOOL_URL = 'https://github.com/impratikjaiswal/pythonHelpers'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/pythonHelpers/issues'
