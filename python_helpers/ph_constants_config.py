from ._git_info import GIT_SUMMARY
from ._tool_name import TOOL_NAME
from ._version import __version__


class PhConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_GIT_SUMMARY = GIT_SUMMARY
