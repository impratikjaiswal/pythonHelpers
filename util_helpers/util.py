import enum
import fnmatch
import inspect
import os
import random
import re
import secrets
import string
from datetime import datetime
from io import TextIOWrapper, StringIO

import math
import pandas as pd
import pkg_resources
import sys
import time
from packaging import version
from pandas import DataFrame

from util_helpers.constants_config import ConfigConst

_base_profiles_available = False
_psutil_available = True
try:
    import psutil
except ImportError:
    _psutil_available = False

from util_helpers.constants import Constants

# path_current_file = os.path.realpath(__file__)
path_current_folder = os.path.realpath(sys.path[0])
path_default_res_folder = path_current_folder + os.sep + 'res'
path_default_log_folder = path_current_folder + os.sep + 'logs'
path_default_out_folder = path_current_folder + os.sep + 'out'
path_default_tst_folder = path_current_folder + os.sep + 'tests'
# Sample Data:
# in Real Environament: D:\ProgramFiles\Python37
# in Virtual Environament: D:\Other\Github_Self\asn1Play\.venv\Scripts
path_python_folder = os.path.split(sys.executable)[0]
path_python_script_folder = os.sep.join([path_python_folder, 'Scripts']) if not path_python_folder.endswith(
    'Scripts') else path_python_folder
path_python_executable = sys.executable


def test(actual, expected):
    """
    Simple provided test() function used in other functions() to print what each function returns vs. what it's supposed to return.
    :param actual: any Object (Actual Output)
    :param expected: any Object (Expected Output)
    :return: None
    """
    if actual == expected:
        prefix = ' OK '
    else:
        prefix = '    X '
    print('%s got: %s, expected: %s' % (prefix, repr(actual), repr(expected)))


# Deprecated
def line_is_comment(str):
    return line_is_comment_or_empty(str)


def line_is_comment_or_empty(str):
    # Check if line is a comment
    comments_pool = ['#', '*', ';', '-', '/*']
    for comment_char in comments_pool:
        if len(str.strip()) == 0 or str.strip().startswith(comment_char):
            return True
    return False


def string_is_blank(str):
    # Check if line is a comment
    return True if str is None or str.strip() == '' else False


def string_is_not_blank(str):
    """

    :param str:
    :return:
    """
    return not string_is_blank(str)


def trim_and_kill_all_white_spaces(str):
    return re.sub(r"\s+", "", str)
    # return str.translate({ord(c): None for c in string.whitespace})


def is_hex(s):
    # Don't verify length here, this is just to verify String Type
    return all(c in string.hexdigits for c in s)


def is_numeric(s):
    return all(c in string.digits for c in s)


def is_ascii(s):
    return all(c in (string.ascii_letters + string.digits) for c in s)


def len_hex(str_hex_data, output_in_str_format=False):
    data_len = int(len(str_hex_data) / 2)
    return '%02X' % data_len if output_in_str_format else data_len


def len_odd(str):
    return True if len(str) % 2 else False


def len_even(str):
    return not len_odd(str)


def swap_nibbles_str(hex_str_data, pad_if_required=True):
    """
    Swap nibbles in a hex string.
    len(s) must be even otherwise ValueError will be raised.
    """
    if len_odd(hex_str_data):
        if pad_if_required:
            hex_str_data = hex_str_data + 'F'
        else:
            raise ValueError()
    return ''.join([y + x for x, y in zip(*[iter(hex_str_data)] * 2)])


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
    if tool_version:
        version_keyword_needed = False if tool_version.strip().lower().startswith('v') else True
        tool_version = f'v{tool_version}' if version_keyword_needed else tool_version
    return ' version is '.join(filter(None, [tool_name, tool_version]))


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


def print_heading(str_heading, char='#', count=80, log=None):
    print_or_log = log.info if log else print
    remaining_count = count - len(str_heading) - 2
    print_or_log(
        ''.join([char * math.ceil(remaining_count / 2), ' ', str_heading, ' ', char * int(remaining_count / 2)]))


def print_data(cmt_to_print, str_hex_data='', log=None):
    return analyse_data(str_hex_data=str_hex_data, cmt_to_print=cmt_to_print, print_also=True, log=log)


def analyse_data(str_hex_data, cmt_to_print='', print_also=False, log=None):
    analysed_str = ''
    if str_hex_data:
        str_hex_data = str(str_hex_data)  # Needed to convert any type
        if len_odd(str_hex_data):
            analysed_str = 'Odd Length'
        analysed_str = ', '.join(filter(None, [analysed_str, 'Length: '
                                               + str(len(str_hex_data)) + ' digits(s) / ' + len_hex(str_hex_data,
                                                                                                    output_in_str_format=True)
                                               + ' byte(s)', 'Data: ' + str_hex_data]))
    if cmt_to_print:
        if str_hex_data:
            cmt_to_print = '\n' + cmt_to_print + '\t'
        analysed_str = ':'.join(filter(None, [cmt_to_print, analysed_str]))
    if print_also:
        print_or_log = log.info if log else print
        print_or_log(analysed_str)
    return analysed_str


def get_file_name_and_extn(file_path, name_with_out_extn=False, only_extn=False, extn_with_out_dot=False,
                           only_path=False, ext_available=True, path_with_out_extn=False, only_folder_name=False):
    """

    :param file_path:
    :param name_with_out_extn:
    :param only_extn:
    :param extn_with_out_dot:
    :param only_path:
    :param path_with_out_extn:

    :return:
    """
    if not file_path:
        return ''
    sep_char = os.sep
    if sep_char == '\\':
        # needed to avoid escape sequence chars in file path
        file_path = re.sub(r'\\{1,}', '/', file_path)
        sep_char = '/'
    split_data = list(filter(None, file_path.split(sep_char)))
    file_name = split_data[-1]
    folder_name = split_data[-2] if len(split_data) > 1 else ''
    path = file_path.replace(file_name, '')
    if only_path:
        path = re.sub(r'/{1,}$', '/', path)
        return path
    if only_folder_name:
        return folder_name
    if ext_available:
        extn = os.path.splitext(file_path)[1]
        if not extn:
            temp = file_path.split(sep_char)[-1]
            if temp[0] == '.':
                extn = temp
    else:
        extn = ''
    if only_extn:
        if extn_with_out_dot:
            return extn.replace('.', '')
        return extn
    file_name_wo_extn = file_name.replace(extn, '')
    # Name is needed
    if name_with_out_extn:
        return file_name_wo_extn
    # Full Name is needed
    if path_with_out_extn:
        return sep_char.join([path, file_name_wo_extn])
    return file_name


def backup_file_name(str_file_path):
    return append_in_file_name(str_file_path, str_append=['backup', get_time_stamp()])


def rreplace(main_str, old, new, max_split=1):
    return new.join(main_str.rsplit(old, max_split))


def append_in_file_name(str_file_path, str_append=None, sep=None, new_name=None, new_ext=None,
                        file_path_is_dir=None, ext_available_in_file_name=None, append_post=None):
    """

    :param str_file_path:
    :param str_append:
    :param sep:
    :param new_name:
    :param new_ext:
    :param file_path_is_dir:
    :param ext_available_in_file_name:
    :param append_post:
    :return:
    """
    # Set Default Values
    if str_append is None:
        str_append = ''
    if sep is None:
        sep = '_'
    if new_ext is None:
        new_ext = ''
    if file_path_is_dir is None:
        file_path_is_dir = False
    if ext_available_in_file_name is None:
        ext_available_in_file_name = True
    if append_post is None:
        append_post = True

    if isinstance(str_file_path, TextIOWrapper):
        str_file_path = str_file_path.name
    if file_path_is_dir or str_file_path.endswith(os.sep):
        str_ext = ''
        str_file_name = ''
        ext_available_in_file_name = False
    else:
        str_ext = get_file_name_and_extn(str_file_path, only_extn=True, ext_available=ext_available_in_file_name)
        str_file_name = get_file_name_and_extn(str_file_path, name_with_out_extn=True,
                                               ext_available=ext_available_in_file_name)
    if isinstance(str_append, list):
        str_append = sep.join(filter(None, str_append))
    if isinstance(new_name, list):
        new_name = sep.join(filter(None, new_name))
    if not str_file_name:
        sep = ''
    if str_append:
        str_append = (sep + str_append) if append_post else (str_append + sep)
    else:
        str_append = ''
    #
    str_new_ext = (str_ext if not new_ext else new_ext)
    str_temp_name = new_name if new_name is not None else str_file_name
    str_new_file_name = (str_temp_name + str_append) if append_post else (str_append + str_temp_name)

    # file name is present
    str_file_path = rreplace(str_file_path, str_file_name, str_new_file_name, 1) if str_file_name else (
            str_file_path + str_new_file_name)

    # extension is present
    str_file_path = rreplace(str_file_path, str_ext, str_new_ext, 1) if str_ext else (str_file_path + str_new_ext)
    return str_file_path


def get_time_stamp(files_format=True, date_only=False):
    if files_format:
        time_format = "%Y%m%d" if date_only else "%Y%m%d_%H%M%S%f"
        # Unique time must be generated
        time.sleep(0.1)
    else:
        time_format = "%Y %m %d" if date_only else "%Y %m %d:%H %M %S %f"
    # current date and time
    now = datetime.now()  # current date and time
    date_time = now.strftime(time_format)
    return str(date_time)


def get_user_friendly_name(python_variable_name):
    temp_data = re.sub(r'[_]', repl=' ', string=python_variable_name)
    return temp_data.title()


def get_python_friendly_name(user_variable_name, all_lower=True):
    if isinstance(user_variable_name, str):
        temp_data = re.sub(r'[ |-]', repl='_', string=user_variable_name)
        return temp_data.lower() if all_lower else temp_data.title()
    return user_variable_name


traverse_modes = ['ImmediateFilesOnly', 'ImmediateFoldersOnly', 'ImmediateFolderAndFiles',
                  'RecursiveFilesOnly', 'RecursiveFoldersOnly', 'RecursiveAll', 'Regex']


def traverse_it(top=path_current_folder, traverse_mode='Regex', include_files=[], include_dirs=[], excludes=[],
                detail_info=False):
    """
    Usage: python <programName.py> <folderName>

    glob: https://en.wikipedia.org/wiki/Glob_(programming)
    :param top:
    :param traverse_mode:
    :param include_files: applicable only when traverseMode is 'Regex'
        Sample: ['*.mp3', '*.mp4']
    :param include_dirs:
    :param excludes: for dirs and files, applicable only when traverseMode is 'Regex'
        Sample1: ['/home/paulo-freitas/Documents']
        Sample2: ["E:\\Entertainment\\Songs_Mp3\\19's", "E:\\Entertainment\\Songs_Mp3\\2000-2009"]
    :param detail_info:
    :return:
    """
    output_list = []
    output_list_temp = []

    print("traverseMode: ", traverse_mode)
    print("top: ", top)

    if traverse_mode == 'Regex':
        # transform glob patterns to regular expressions
        include_files = r'|'.join([fnmatch.translate(x) for x in include_files])
        include_dirs = r'|'.join([fnmatch.translate(x) for x in include_dirs])
        excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
        print("include_files: ", include_files)
        print("include_dirs: ", include_dirs)
        print("excludes: ", excludes)

    for dirpath, dirnames, filenames in os.walk(top):
        if traverse_mode == 'ImmediateFilesOnly':
            for filename in filenames:
                if dirpath == top:
                    filepath = os.path.join(dirpath, filename)
                    output_list.append(filepath)

        if traverse_mode == 'ImmediateFoldersOnly':
            for dirname in dirnames:
                if dirpath == top:
                    filepath = os.path.join(dirpath, dirname)
                    output_list.append(filepath)

        if traverse_mode == 'ImmediateFolderAndFiles':
            output_list_temp = traverse_it(top, traverse_mode='ImmediateFoldersOnly')
            output_list = output_list_temp
            output_list_temp = traverse_it(top, traverse_mode='ImmediateFilesOnly')
            output_list = output_list + output_list_temp

        if traverse_mode == 'RecursiveFilesOnly':
            for filename in filenames:
                try:
                    filepath = os.path.join(dirpath, filename)
                    if detail_info:
                        filesize = str_insert_char_repeatedly(os.stat(filepath).st_size, reverse=True)
                        fileext = get_file_name_and_extn(filename, only_extn=True, extn_with_out_dot=True)
                        pattern = [filename, filepath, filesize, fileext]
                        output_list.append("\t".join(pattern))
                    else:
                        output_list.append(filepath)
                except:
                    pass

        if traverse_mode == 'RecursiveFoldersOnly':
            for dirname in dirnames:
                filepath = os.path.join(dirpath, dirname)
                output_list.append(filepath)

        if traverse_mode == 'RecursiveAll':
            output_list_temp = traverse_it(top, traverse_mode='RecursiveFoldersOnly')
            output_list = output_list_temp
            output_list_temp = traverse_it(top, traverse_mode='RecursiveFilesOnly')
            output_list = output_list + output_list_temp

        if traverse_mode == 'Regex':
            # Ref: https://stackoverflow.com/a/5141829

            # exclude dirs
            dirnames[:] = [os.path.join(dirpath, d) for d in dirnames]
            dirnames[:] = [d for d in dirnames if not re.match(excludes, d)]
            # include dirs
            dirnames[:] = [d for d in dirnames if re.match(include_dirs, d)]
            # exclude/include filenames
            filenames = [os.path.join(dirpath, f) for f in filenames]
            filenames = [f for f in filenames if not re.match(excludes, f, re.IGNORECASE)]
            filenames = [f for f in filenames if re.match(include_files, f, re.IGNORECASE)]
            output_list = output_list + filenames
    return output_list


def get_random_string_for_variable(var_name):
    """

    :param var_name:
    :return:
    """
    var_name = get_synonym_of_variable_name(var_name)
    if var_name in Constants.POOL_4_DIGITS_LENGTH:
        size = 4
        str_type = Constants.STR_TYPE_NUMERIC
    elif var_name in Constants.POOL_8_DIGITS_LENGTH:
        size = 8
        str_type = Constants.STR_TYPE_NUMERIC
    elif var_name in Constants.POOL_16_BYTES_LENGTH:
        size = 16
        str_type = Constants.STR_TYPE_HEX
    else:
        return ''
    return get_random_string(size, str_type)


def get_random_string(target_str_length=8, str_type=Constants.STR_TYPE_HEX):
    """

    :param target_str_length:
    :param str_type:
    :return:
    """
    if str_type == Constants.STR_TYPE_PLAIN:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(target_str_length))
    if str_type == Constants.STR_TYPE_HEX:
        return secrets.token_hex(target_str_length).upper()
    if str_type == Constants.STR_TYPE_NUMERIC:
        letters = string.digits
    return ''.join(random.choice(letters) for _ in range(target_str_length))


def get_synonym_of_variable_name(var_name, var_type=Constants.VAR_TYPE_OUT):
    """

    :param var_name:
    :param var_type:
    :return:
    """
    default_offset = (1 if var_type == Constants.VAR_TYPE_PROFILE else 0)
    pools = [
        Constants.VAR_POOL_ICCID, Constants.VAR_POOL_IMSI, Constants.VAR_POOL_IMSI2, Constants.VAR_POOL_KI,
        #
        Constants.VAR_POOL_PIN1, Constants.VAR_POOL_PIN2, Constants.VAR_POOL_2_PIN1, Constants.VAR_POOL_3_PIN1,
        #
        Constants.VAR_POOL_PUK1, Constants.VAR_POOL_PUK2, Constants.VAR_POOL_2_PUK1, Constants.VAR_POOL_3_PUK1,
        #
        Constants.VAR_POOL_ADM1, Constants.VAR_POOL_ADM2, Constants.VAR_POOL_ADM3,
        #
        Constants.VAR_POOL_ACC,
        #
        Constants.VAR_POOL_KIC1, Constants.VAR_POOL_KID1, Constants.VAR_POOL_KIK1,
        #
        Constants.VAR_POOL_KIC2, Constants.VAR_POOL_KID2, Constants.VAR_POOL_KIK2,
        #
        Constants.VAR_POOL_MNO_SD_KIC_01, Constants.VAR_POOL_MNO_SD_KID_01, Constants.VAR_POOL_MNO_SD_KIK_01,
        #
        Constants.VAR_POOL_MNO_SD_KIC_02, Constants.VAR_POOL_MNO_SD_KID_02, Constants.VAR_POOL_MNO_SD_KIK_02,
        #
        Constants.VAR_POOL_MNO_SD_KIC_03, Constants.VAR_POOL_MNO_SD_KID_03, Constants.VAR_POOL_MNO_SD_KIK_03,
        #
        Constants.VAR_POOL_MNO_SD_KIC_04, Constants.VAR_POOL_MNO_SD_KID_04, Constants.VAR_POOL_MNO_SD_KIK_04,
        #
        Constants.VAR_POOL_MNO_SD_KIC_05, Constants.VAR_POOL_MNO_SD_KID_05, Constants.VAR_POOL_MNO_SD_KIK_05,
        #
        Constants.VAR_POOL_MNO_SD_KIC_06, Constants.VAR_POOL_MNO_SD_KID_06, Constants.VAR_POOL_MNO_SD_KIK_06,
        #
        Constants.VAR_POOL_MNO_SD_KIC_07, Constants.VAR_POOL_MNO_SD_KID_07, Constants.VAR_POOL_MNO_SD_KIK_07,
        #
        Constants.VAR_POOL_MNO_SD_KIC_08, Constants.VAR_POOL_MNO_SD_KID_08, Constants.VAR_POOL_MNO_SD_KIK_08,
        #
        Constants.VAR_POOL_MNO_SD_KIC_09, Constants.VAR_POOL_MNO_SD_KID_09, Constants.VAR_POOL_MNO_SD_KIK_09,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0A, Constants.VAR_POOL_MNO_SD_KID_0A, Constants.VAR_POOL_MNO_SD_KIK_0A,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0B, Constants.VAR_POOL_MNO_SD_KID_0B, Constants.VAR_POOL_MNO_SD_KIK_0B,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0C, Constants.VAR_POOL_MNO_SD_KID_0C, Constants.VAR_POOL_MNO_SD_KIK_0C,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0D, Constants.VAR_POOL_MNO_SD_KID_0D, Constants.VAR_POOL_MNO_SD_KIK_0D,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0E, Constants.VAR_POOL_MNO_SD_KID_0E, Constants.VAR_POOL_MNO_SD_KIK_0E,
        #
        Constants.VAR_POOL_MNO_SD_KIC_0F, Constants.VAR_POOL_MNO_SD_KID_0F, Constants.VAR_POOL_MNO_SD_KIK_0F,
        #
    ]
    for pool in pools:
        if var_name in pool:
            return pool[default_offset]
    return var_name


def generate_range_str(start_point, end_point, func=None):
    range_data = []
    start_counter = int(start_point[len(start_point) - Constants.MAX_SUPPORTED_DIGIT_IN_INT:])
    end_counter = int(end_point[len(end_point) - Constants.MAX_SUPPORTED_DIGIT_IN_INT:])
    start_point = start_point[:-Constants.MAX_SUPPORTED_DIGIT_IN_INT]
    for count in range(start_counter, end_counter + 1):
        data = start_point + str(count).zfill(Constants.MAX_SUPPORTED_DIGIT_IN_INT)
        if func:
            data = func(data)
        range_data.append(data)
    return range_data


def makedirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def find_offset_of_section(data, char_to_find, corresponding_char_to_find):
    """
    Considering Ideal Scenario: Any target char is not present as a comment
    Data Pattern is correct,target characters are available in pairs

    :param data:
    :param char_to_find:
    :param corresponding_char_to_find:
    :return:
    """
    slack = []
    start_char_list = [m.start() for m in re.finditer(char_to_find, data)]
    end_char_list = [m.start() for m in re.finditer(corresponding_char_to_find, data)]
    start_char_list_len = len(start_char_list)
    end_char_list_len = len(end_char_list)
    # print('start_char_list', start_char_list)
    # print('end_char_list', end_char_list)
    # print('start_char_list_len', start_char_list_len)
    # print('end_char_list_len', end_char_list_len)
    index_start_char = 0
    index_end_char = 0
    count = 0
    end_char = len(data)  # assignment is needed for the wrong case when target chars are not present
    while count < start_char_list_len + end_char_list_len:
        count += 1
        start_char = int(start_char_list[index_start_char]) if index_start_char < start_char_list_len else -1
        end_char = int(end_char_list[index_end_char]) if index_end_char < end_char_list_len else -1
        if start_char < end_char and start_char != -1:
            # print('pushed', start_char)
            index_start_char += 1
            slack.append(start_char)
        else:
            # print('poped', end_char)
            index_end_char += 1
            slack.pop()
        if len(slack) == 0:
            # print(corresponding_char_to_find, end_char)
            break;
    return end_char


def dec_to_hex(dec_num, digit_required=None, even_digits=True):
    # return hex(dec_num).split('x')[-1].upper()
    # return '0x{:02x}'.format(dec_num)
    # return binascii.hexlify(str(dec_num))
    if digit_required is None:
        digit_required = 0
    temp = format(dec_num, 'X')
    if even_digits:
        temp = temp.rjust(len(temp) + (1 if len_odd(temp) else 0), '0')
    return temp.rjust(digit_required, '0')


def hex_str_to_dec(hex_str):
    if isinstance(hex_str, str):
        return int(hex_str, 16)
    return hex_str


def hex_str_to_hex_list(hex_str):
    hex_str = trim_and_kill_all_white_spaces(hex_str)
    chunk_size = 2
    return [hex_str_to_dec(hex_str[i:i + chunk_size]) for i in range(0, len(hex_str), chunk_size)]


def rstrip_hex_str(hex_str):
    return rstrip_str(hex_str, 'FF')


def rstrip_str(plain_str, data_to_strip):
    # data = data.rstrip('FF')
    # data = data[:data.rfind("FF$")]
    # Must be removed in pair
    # pattern = '(FF)*$'
    pattern = '(' + data_to_strip + ')*$'
    return re.sub(pattern, '', plain_str)


def lstrip_hex_str(hex_str):
    return lstrip_str(hex_str, 'FF')


def lstrip_str(plain_str, data_to_strip):
    pattern = '^(' + data_to_strip + ')*'
    return re.sub(pattern, '', plain_str)


def analyse_profile(base_profile, imp_info=False):
    if isinstance(base_profile, bytes):
        base_profile = base_profile.hex()
    bp_name = ''
    bp_status = False
    if _base_profiles_available:
        for key in base_profiles.profile_pool_hex:
            if base_profiles.profile_pool_hex.get(key).lower() in base_profile.lower():
                bp_name = key
                bp_status = True
                break
    # Logic is needed to analyse Custom Profiles
    msg = [f'Profile Name is: {bp_name}{" (Base Profile)" if bp_status else ""}']
    if imp_info:
        module_name = Constants.MODULE_PYCRATE_NAME
        module_version = get_module_version(module_name)[0]
        msg.append(
            f'\n',
            f'Important Info: ',
            f'{module_name} version is: {module_version}',
        )
    return '\n'.join(msg), bp_status


def get_key_from_dict_based_on_val(my_dict, value_to_check, operation=None):
    for key, value in my_dict.items():
        if operation == 'startswith':
            if value_to_check.startswith(value):
                return key
        elif value == value_to_check:
            return key
    return None


def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print('File {0} deleted successfully.'.format(file_path))
    else:
        print('File {0} does not exist.'.format(file_path))


def get_current_func_name():
    # print(inspect.stack()[0][3])  # will give current
    # print(inspect.stack()[1][3])  # will give the caller (Parent)
    return inspect.stack()[1][3]


ENCLOSE_HEX = 1
ENCLOSE_NAME_VALUE = 2
ENCLOSE_NAME_VALUE_HEX = 3
ENCLOSE_NAME_VALUE_DICT = 4
ENCLOSE_NAME_VALUE_HEX_DICT = 5
ENCLOSE_NAME_VALUE_SEQ_DICT = 6
ENCLOSE_NAME_VALUE_SEQ = 7
ENCLOSE_COMMENT = 8


def enclose(format, data1, data2='', indent_level=0):
    space = '  ' * indent_level
    if format == ENCLOSE_COMMENT:
        return space + "-- " + str(data1)
    if format == ENCLOSE_HEX:
        return space + "'" + str(data1) + "'H"
    if format == ENCLOSE_NAME_VALUE:  # identification 0
        return space + data1 + ' ' + data2
    if format == ENCLOSE_NAME_VALUE_HEX:  # efFileSize '68'H
        return space + data1 + ' ' + enclose(ENCLOSE_HEX, data2)
    if format == ENCLOSE_NAME_VALUE_DICT:  # doNotCreate : NULL
        return space + data1 + ' : ' + data2
    if format == ENCLOSE_NAME_VALUE_HEX_DICT:  # filePath : '7FF1'H
        return space + data1 + ' : ' + enclose(ENCLOSE_HEX, data2)
    if format in [ENCLOSE_NAME_VALUE_SEQ, ENCLOSE_NAME_VALUE_SEQ_DICT]:  # templateID {0 0} # fileDescriptor : {...}
        separator = ' ' if format == ENCLOSE_NAME_VALUE_SEQ else ' : '
        if data1 == '':
            separator = ''
        if isinstance(data2, str):
            return space + data1 + separator + '{' + data2 + '}'
        if isinstance(data2, list):
            if len(data2) == 0:  # Empty List
                return space + data1 + separator + '{ }'
            return space + data1 + separator + '{\n' + ',\n'.join(data2) + '\n' + space + '}'
    return data1


def normalise_name_user_to_pandas(col_name, upper_case=True, fix_names=[]):
    # Remove unwanted var_out
    res_items = [ele for ele in Constants.KEYWORD_VARIABLE_DECLARATION_OUT if (ele in col_name)]
    for item in res_items:
        col_name = col_name.replace(item, '')
    # Remove these Chars
    temp_data = re.sub(r'[(]|[)]|[.]|[:]', repl='', string=col_name)
    # Strip Unnecessary White Spaces
    temp_data = temp_data.strip()
    # Replace these Chars
    temp_data = re.sub(r'[ ]|[/]', repl='_', string=temp_data)
    # Remove Multiple Occurrences Of '_'
    temp_data = re.sub(r'[_]+', repl='_', string=temp_data)
    # Convert the case
    if fix_names:
        temp_fix_names = [each_string.lower() for each_string in fix_names]
        if temp_data.lower() in temp_fix_names:
            return fix_names[temp_fix_names.index(temp_data.lower())]
    temp_data = temp_data.upper() if upper_case else temp_data.lower()
    return temp_data


def normalise_name_pandas_to_user(col_name, all_caps_keywords=None):
    """

    :param col_name:
    :param all_caps_keywords:
    :return:
    """
    if all_caps_keywords is None:
        all_caps_keywords = ['ICCID', 'IMSI', 'ID', 'MSISDN']
    return ' '.join(
        x.title() if x not in all_caps_keywords else x for x in [x for x in re.split('_', string=str(col_name))])


def read_csv(file_name, sep='\s+', rename_col=False, comment='*', print_shape=True, print_frame=False
             # , encoding='unicode_escape'
             , names=None
             , encoding=None
             , log=None):
    if names:
        obj = pd.read_csv(file_name, sep=sep, dtype='str', na_filter=False, skip_blank_lines=True, comment=comment,
                          encoding=encoding, names=names)
    else:
        obj = pd.read_csv(file_name, sep=sep, dtype='str', na_filter=False, skip_blank_lines=True, comment=comment,
                          encoding=encoding)
    #
    rename_col_dict = {}
    if rename_col:
        # Fixing Messy Column Names
        for col_name in list(obj):
            rename_col_dict[col_name] = normalise_name_user_to_pandas(col_name)
        obj.rename(columns=rename_col_dict, inplace='True')
    if print_shape:
        print_data_frame_shape(obj, '' if isinstance(file_name, StringIO) else file_name, log=log)
    if print_frame:
        print_data_frame(obj, log=log)
    return obj


def to_csv(output, file_name, str_append='', new_ext='', sep=' ', index=False, print_shape=True, print_frame=False,
           encoding=None, log=None):
    if print_shape:
        print_data_frame_shape(output, file_name, log=log)
    if print_frame:
        print_data_frame(output)
    if str_append or new_ext:
        file_name = append_in_file_name(str_file_path=file_name, str_append=str_append, new_ext=new_ext)
    makedirs(get_file_name_and_extn(file_name, only_path=True))
    output.to_csv(path_or_buf=file_name, index=index, sep=sep, encoding=encoding)
    return file_name


def compare_two_data_frame(file_input_left, file_input_right, col_name, file_result='', sort=False, print_shape=True,
                           print_frame=False, encoding=None, log=None):
    local_data_left = file_input_left if isinstance(file_input_left, DataFrame) else \
        read_csv(file_input_left, sep=',', encoding=encoding, log=log)
    local_data_right = file_input_right if isinstance(file_input_right, DataFrame) else \
        read_csv(file_input_right, sep=',', encoding=encoding, log=log)
    file_output_left = ''
    file_output_common = ''
    file_output_right = ''
    if not file_result:
        file_result = append_in_file_name(
            str_file_path=append_in_file_name(
                str_file_path=os.sep.join([path_default_out_folder, '']),
                str_append=[col_name, '1st'], new_ext='.txt')
            if isinstance(file_input_left, DataFrame) else file_input_left,
            str_append=['vs', ('2nd' if isinstance(file_input_right, DataFrame) else
                               get_file_name_and_extn(file_input_right, name_with_out_extn=True))])
    """
    Left
    """
    file_output_left = append_in_file_name(str_file_path=file_result, str_append='left')
    # outData = local_data_left[~local_data_left.col_name.isin(local_data_right.col_name)] # Getting error for this
    out_data = local_data_left[~local_data_left[col_name].isin(local_data_right[col_name])]
    out_data.to_csv(path_or_buf=file_output_left, index=False)
    if sort:
        file_output_left = append_in_file_name(str_file_path=file_output_left, str_append='sorted')
    out_data = out_data.sort_values(by=col_name)
    out_data.to_csv(path_or_buf=file_output_left, index=False)
    if print_shape:
        print_data_frame_shape(out_data, file_output_left, log=log)
    if print_frame:
        print_data_frame(out_data, log=log)
    """
    Right
    """
    file_output_right = append_in_file_name(str_file_path=file_result, str_append='right')
    out_data = local_data_right[~local_data_right[col_name].isin(local_data_left[col_name])]
    out_data.to_csv(path_or_buf=file_output_right, index=False)
    if sort:
        file_output_right = append_in_file_name(str_file_path=file_output_right, str_append='sorted')
    out_data = out_data.sort_values(by=col_name)
    out_data.to_csv(path_or_buf=file_output_right, index=False)
    if print_shape:
        print_data_frame_shape(out_data, file_output_right, log=log)
    if print_frame:
        print_data_frame(out_data, log=log)
    """
    Common
    """
    file_output_common = append_in_file_name(str_file_path=file_result, str_append='common')
    out_data = local_data_left[local_data_left[col_name].isin(local_data_right[col_name])]
    out_data.to_csv(path_or_buf=file_output_common, index=False)
    if sort:
        file_output_common = append_in_file_name(str_file_path=file_output_common, str_append='sorted')
        out_data = out_data.sort_values(by=col_name)
        out_data.to_csv(path_or_buf=file_output_common, index=False)
    if print_shape:
        print_data_frame_shape(out_data, file_output_common, log=log)
    if print_frame:
        print_data_frame(out_data, log=log)
    return file_output_left, file_output_common, file_output_right


def strip_all_columns(df_input):
    df_obj = df_input.select_dtypes(['object'])
    df_input[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df_input


"""
    Help: Print
    options:
    print(list(output))
    output.info()
    print(output)
    print(output.head())
    print(output[['ICCID']])
    print(output['ICCID'].head())

"""


def print_data_frame(output, cmt='', level=0, log=None):
    if not isinstance(output, DataFrame):
        return
    pd.set_option('display.max_columns', None)
    print_or_log = log.info if log else print
    # pd.set_option('display.max_rows', None)
    print_or_log(cmt)
    if level == 0:
        print_or_log(output.head())
    if level == 1:
        print_or_log(output.tail())
    if level == 2:
        print_or_log(output.to_string(index=False))
    if level == 3:
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print_or_log(output)


def print_data_frame_shape(output, cmt='', level=1, log=None):
    if not isinstance(output, DataFrame):
        return
    count_row, count_col = output.shape
    print_or_log = log.info if log else print
    print_or_log(','.join(filter(None, ["Shape: {} x {}".format(count_row, count_col), cmt])))
    # Faster alternate
    # count_row = len(output.index)
    if level < 1:
        return
    print_or_log(list(output))
    if level < 2:
        return
    print_or_log(output.info())


def find_offset_of_next_non_white_space_char(temp, current_offset):
    new_offset = current_offset
    for a in temp[current_offset:]:
        if not a.isspace():
            break
        new_offset += 1
    return new_offset


def str_insert_char_repeatedly(my_str, group=3, char=',', reverse=False):
    my_str = str(my_str)
    start = 0
    end = len(my_str)
    pre_str = ''
    post_str = ''
    if reverse:
        start = end % group
        pre_str = my_str[0:start]
    post_str = char.join(my_str[i:i + group] for i in range(start, end, group))
    return char.join(filter(None, [pre_str, post_str]))


def prepare_file_name(keywords_list, file_ext='.txt', time_stamp=True):
    sep = '_'
    file_name = keywords_list
    time_str = get_time_stamp(files_format=True) if time_stamp else ''
    if isinstance(keywords_list, list):
        keywords_list.append(time_str)
        file_name = sep.join(filter(None, keywords_list))
    sep = ''
    return sep.join([file_name, file_ext])


def format_profile_parsing_log(profile_hex_data, profiles_asn_data, profile_name=None):
    """

    :param profile_hex_data:
    :param profiles_asn_data:
    :param profile_name:
    :return: dict with log_folder, log_name, log_data
    """
    if not profile_name:
        profile_name = 'Profile'
    full_logging = True if (profile_hex_data and profiles_asn_data) else False
    logging_data_list = []
    file_ext = '.txt'
    log_folder = None
    file_name_keywords = []
    if full_logging:
        res_profile_name, res_bp_status = analyse_profile(profile_hex_data)
        logging_data_list.append(res_profile_name)
        logging_data_list.append('\n\n' + 'Hex Profile is: \n')
    else:  # Any one is definitely True
        if not profile_hex_data:
            log_folder = 'asn1'
            file_ext = '.asn1'
        if not profiles_asn_data:
            log_folder = 'hex'
            file_ext = '.hex'
    log_name = append_in_file_name(str_file_path=profile_name, str_append=file_name_keywords, new_ext=file_ext,
                                   # Profile name could have a '.'
                                   ext_available_in_file_name=False)
    if profile_hex_data:
        logging_data_list.append(profile_hex_data)
    if full_logging:
        logging_data_list.append('\n\n' + 'ASN Profile is: \n')
    if profiles_asn_data:
        logging_data_list.append(profiles_asn_data)
    return {
        'log_folder': log_folder,
        'log_name': log_name,
        'log_content': ''.join(logging_data_list),
    }


def ascii_to_hex_str(ascii_str):
    return ascii_str.encode('utf-8').hex()


def hex_str_to_ascii(str):
    # Check if printable
    hex_bytes = [hex_str_to_dec(str[i:i + 2]) for i in range(0, len(str), 2)]
    printable = all((0x20 <= hex_byte <= 0x7E) for hex_byte in hex_bytes)
    return bytearray.fromhex(str).decode() if printable else ''


def gen_acc(str_imsi):
    # formula: 2 ^ imsi_last_digit
    return dec_to_hex(pow(2, int(str_imsi[-1])), 4)


def gen_isim_data(imsi, mcc_mnc, pattern_or_data):
    """

    :param imsi:
    :param mcc_mnc:
    :param pattern: Could be pattern as well as real data
    :return:
    """
    if pattern_or_data is not None:
        mcc = ''
        mnc = ''
        if mcc_mnc is not None:
            mcc = mcc_mnc[0:3]
            # MNC must be padded with 0 if needed
            mnc = mcc_mnc[3:].zfill(3)
        pattern_or_data = pattern_or_data.replace('${IMSI}', imsi)
        pattern_or_data = pattern_or_data.replace('${MCC}', mcc)
        pattern_or_data = pattern_or_data.replace('${MNC}', mnc)
    return pattern_or_data


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


def check_and_assign(primary_value, secondry_value):
    if primary_value is not None:
        return primary_value
    if secondry_value is not None:
        return secondry_value
    return None


def get_version_from_name(name, max_depth=None, trim_v=False):
    if max_depth is None:
        match = re.search('(v|V)([\d._-])*(\d)', name)
    else:
        match = re.search('(v|V)([\d._-]){0,' + str(max_depth + 1) + '}(\d)', name)
    if match:
        result = re.sub('[._-]', '_', match.group(0))
        return result[1:] if trim_v else result
    return ''


def print_all_environment_variables(custom_only=False):
    if custom_only:
        for var in Constants.ENV_VARIABLES:
            print(get_environment_variables(var))
    else:
        print_iter(os.environ)


def str_to_bool(value):
    if isinstance(value, bool):
        return value
    value = value.lower().strip()
    if value in Constants.TRUE_VALUE_POOL:
        return True
    elif value in Constants.FALSE_VALUE_POOL:
        return False
    return None


def is_clean_name(name):
    return not name.startswith('_') and not name.endswith('_')


def clean_names(lst):
    return [n for n in lst if is_clean_name(n)]


def get_obj_list(cls_to_explore, obj_name_filter, obj_name_needed=False, obj_value_to_find=None, clean_name=False,
                 sort=False):
    if cls_to_explore is None:
        return ''
    obj_list = [obj if obj_name_needed else getattr(cls_to_explore, obj)
                for obj in cls_to_explore.__dict__ if str(obj).startswith(obj_name_filter)]
    if clean_name:
        obj_list = clean_names(obj_list)
    if sort:
        obj_list.sort()
    if len(obj_list) > 0 and isinstance(obj_list[0], list):
        obj_list = obj_list[0]
    if isinstance(cls_to_explore, enum.EnumMeta):
        obj_list = [cls_to_explore(obj).name for obj in obj_list]
    if obj_value_to_find is None:
        return obj_list
    for obj in obj_list:
        if obj.value == obj_value_to_find:
            return obj.name
    return ''


def normalise_user_input(user_input):
    temp_user_input = str_to_bool(user_input)
    if temp_user_input is not None:
        return temp_user_input
    if user_input in Constants.EXIT_VALUE_POOL:
        # return 'e'
        sys.exit()
    print(f'Oops! "{user_input}" was not a valid input. Try again...')
    return None


def get_environment_variables(var_name, check_presence_only=False):
    # Check for Custom Variables
    env_variable_name, env_variable_default_value = Constants.ENV_VARIABLES.get(var_name, (None, None))
    if env_variable_name is None:
        env_variable_name = var_name
    try:
        env_variable_value = os.environ[env_variable_name]
        if check_presence_only:
            return True
        print(f'Environment Variable {env_variable_name} Found, value is {env_variable_value}')
    except:
        if check_presence_only:
            return False
        print(f'Environment Variable {env_variable_name} Not Found, using default Value {env_variable_default_value}')
        env_variable_value = env_variable_default_value
    return env_variable_value


def format_data_as_hex(str_data):
    return ' '.join(re.findall('([0-9a-zA-Z]{2}|[0-9a-zA-Z])', str_data))


def append_path(dir_file_list):
    return os.sep.join(filter(None, dir_file_list))


def cpu_usage():
    if _psutil_available:
        res = psutil.cpu_times()
        print(f'cpu_times is {res}')

        res = psutil.cpu_percent(0.1)
        print(f'cpu_percent is {res}')

        res = psutil.cpu_times_percent(0.1)
        print(f'cpu_times_percent is {res}')

        res = psutil.cpu_stats()
        print(f'cpu_stats is {res}')

        res = psutil.cpu_freq()
        print(f'cpu_freq is {res}')

        res = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        print(f'getloadavg is {res}')


def get_module_version(module_name=Constants.MODULE_PYCRATE_NAME, minimum_version_required=None):
    module_version = pkg_resources.get_distribution(module_name).version
    module_version = version.parse(module_version)
    res = None
    if minimum_version_required:
        minimum_version_required = version.parse(minimum_version_required)
        res = True if module_version >= minimum_version_required else False
    return module_version, res
