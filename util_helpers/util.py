import re
import string
import sys

import pkg_resources
from packaging import version

from util_helpers.constants import Constants
from util_helpers.constants_config import ConfigConst


def trim_and_kill_all_white_spaces(str):
    return re.sub(r"\s+", "", str)
    # return str.translate({ord(c): None for c in string.whitespace})


def is_hex(s):
    # Don't verify length here, this is just to verify String Type
    return all(c in string.hexdigits for c in s)


def check_if_iter(the_iter):
    if the_iter is None:
        return False, the_iter
    # Duck Typing
    try:
        # Check if iterable, but not String as String is also iterable
        if isinstance(the_iter, str):
            is_iter = False
        else:
            iter(the_iter)
            is_iter = True
    except TypeError:
        try:
            # Check if dict attribute is present but obj is not iterable by default, e.g: Namespace
            the_iter = the_iter.__dict__
            is_iter = True
        except AttributeError:
            is_iter = False
    return is_iter, the_iter


def print_iter(the_iter, header=None, log=None, list_as_str=None):
    """
    This function takes a positional argument called "the_iter", which is any
        Python list (of, possibly, nested lists). Each data item in the provided list
        is (recursively) printed to the screen on its own line.
    :param the_iter:
    :param header:
    :param log:
    :param list_as_str:
    :return:
    """
    print_or_log = log.info if log else print
    list_as_str = False if list_as_str is None else list_as_str
    is_iter, the_iter = check_if_iter(the_iter)
    if header:
        header = f'{header}:'
    if (list_as_str and isinstance(the_iter, list)) or not is_iter:
        print_or_log(' '.join(filter(None, [header, str(the_iter)])))
        return
    if header:
        print_or_log(header)
    # Iterable is Dictionary
    if isinstance(the_iter, dict):
        for key in the_iter.keys():
            value = the_iter[key]
            if check_if_iter(value)[0]:
                print_iter(the_iter=value, header=str(key), log=log, list_as_str=list_as_str)
            else:
                print_or_log(f'{str(key)}: {value}')
        return
    # Other iterable Items
    for each_item in the_iter:
        # Check if sub-objects are Iterable
        if check_if_iter(each_item)[0]:
            print_iter(the_iter=each_item, log=log)
            continue
        print_or_log(each_item)


def print_separator(character='-', count=80, main_text='', log=None, get_only=False):
    print_or_log = log.info if log else print
    if main_text is None:
        main_text = ''
    text_len = len(main_text)
    if count - 4 <= text_len:
        count = 2  # Minimum Needed
    else:
        count = count - text_len
    count = int(count / 2)
    sep_initial = count * character
    sep_end = count * character
    sep_mid = ' ' if main_text else ''
    msg = f'{sep_initial}{sep_mid}{main_text}{sep_mid}{sep_end}'
    if get_only:
        return msg
    print_or_log(msg)


def print_done(log=None):
    print_separator(log=log)
    print_separator(character=' ', count=35, main_text='All Done.', log=log)
    print_separator(log=log)


def print_error(str_heading, log=None):
    print_separator(log=log)
    print_separator(main_text=f'Error Occured: {str_heading}', log=log)
    print_separator(log=log)


def get_tool_name_w_version(tool_name=None, tool_version=None):
    return ' version is '.join(filter(None, [tool_name, f'v{tool_version}' if tool_version else None]))


def print_version(tool_name, tool_version, with_python_version=True, log=None):
    print_or_log = log.info if log else print
    print_separator(log=log)
    if with_python_version:
        print_or_log(f'Python version is {sys.version}')
    print_or_log(get_tool_name_w_version(tool_name=tool_name, tool_version=tool_version))
    print_separator(log=log)


def print_version_pkg(package_name=ConfigConst.TOOL_NAME, package_version=ConfigConst.TOOL_VERSION,
                      with_python_version=True, log=None):
    print_version(tool_name=package_name, tool_version=package_version, with_python_version=with_python_version,
                  log=log)


def hex_str_to_dec(hex_str):
    if isinstance(hex_str, str):
        return int(hex_str, 16)
    return hex_str


def to_hex_string(bytes=[], format=0):
    """Returns a hex string representing bytes

    @param bytes:  a list of bytes to stringify,
                e.g. [59, 22, 148, 32, 2, 1, 0, 0, 13]
    @param format: a logical OR of
      - COMMA: add a comma between bytes
      - HEX: add the 0x chars before bytes
      - UPPERCASE: use 0X before bytes (need HEX)
      - PACK: remove blanks
    """

    if type(bytes) is not list:
        raise TypeError('not a list of bytes')

    if bytes is None or bytes == []:
        return ""
    else:
        pformat = "%-0.2X"
        if Constants.FORMAT_HEX_STRING_AS_COMMA & format:
            separator = ","
        else:
            separator = ""
        if not Constants.FORMAT_HEX_STRING_AS_PACK & format:
            separator = separator + " "
        if Constants.FORMAT_HEX_STRING_AS_HEX & format:
            if Constants.FORMAT_HEX_STRING_AS_UPPERCASE & format:
                pformat = "0X" + pformat
            else:
                pformat = "0x" + pformat
        return (separator.join(map(lambda a: pformat % ((a + 256) % 256), bytes))).rstrip()


def get_module_version(module_name=Constants.MODULE_PYCRATE_NAME, minimum_version_required=None):
    module_version = pkg_resources.get_distribution(module_name).version
    module_version = version.parse(module_version)
    res = None
    if minimum_version_required:
        minimum_version_required = version.parse(minimum_version_required)
        res = True if module_version >= minimum_version_required else False
    return module_version, res
