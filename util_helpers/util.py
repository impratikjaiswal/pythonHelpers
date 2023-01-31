import os
import re
import string
import sys
from io import TextIOWrapper

import pkg_resources
from packaging import version

from util_helpers.constants import Constants

# path_current_file = os.path.realpath(__file__)
path_current_folder = os.path.realpath(sys.path[0])
path_default_res_folder = path_current_folder + os.sep + 'res'
path_default_log_folder = path_current_folder + os.sep + 'logs'
path_default_out_folder = path_current_folder + os.sep + 'out'
path_default_tst_folder = path_current_folder + os.sep + 'tests'
from util_helpers.constants_config import ConfigConst


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
                           only_path=False, ext_available=True, path_with_out_extn=False):
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
        file_path = file_path.replace('\\', '/')
        sep_char = '/'
    file_name = file_path.split(sep_char)[-1]
    path = file_path.replace(file_name, '')
    if only_path:
        return path
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
    str_file_path = str_file_path.replace(str_file_name, str_new_file_name) if str_file_name else (
            str_file_path + str_new_file_name)

    # extension is present
    str_file_path = str_file_path.replace(str_ext, str_new_ext) if str_ext else (str_file_path + str_new_ext)
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


def makedirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)



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


def get_module_version(module_name=Constants.MODULE_PYCRATE_NAME, minimum_version_required=None):
    module_version = pkg_resources.get_distribution(module_name).version
    module_version = version.parse(module_version)
    res = None
    if minimum_version_required:
        minimum_version_required = version.parse(minimum_version_required)
        res = True if module_version >= minimum_version_required else False
    return module_version, res
