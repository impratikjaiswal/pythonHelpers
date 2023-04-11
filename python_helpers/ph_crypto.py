import binascii
from Crypto.Cipher import AES
from itertools import cycle

from python_helpers import ph_util


def logical_xor_(hex_str_msg, hex_str_key):
    """
    Logical XOR among two hex String
    :param hex_str_msg: Main Message as Hex Str
    :param hex_str_key: Key as Hex Str
    :return: output as hex String
    """
    # Convert to Binary
    bin_str_msg = bytearray.fromhex(hex_str_msg)
    bin_str_key = bytearray.fromhex(hex_str_key)
    data = bytearray()
    # Cycle of key is needed for scenario when len(data) > len(key)
    for c, k in zip(bin_str_msg, cycle(bin_str_key)):
        data.append(c ^ k)
    data = data.hex().upper()
    # print('data' + data)
    return data


def logical_xor(str1_hex, str2_hex):
    """

    :param str1_hex:
    :param str2_hex:
    :return:
    """
    if len(str1_hex) != len(str2_hex):
        return False
    data = bytearray(
        [x ^ y for x, y in zip(bytearray.fromhex(str1_hex), bytearray.fromhex(str2_hex))]).hex().upper()
    return data


def aes_encrypt(hex_strkey, hex_str_buff, algo=AES.MODE_CBC, hex_str_iv='00000000000000000000000000000000'):
    """
    AES Encryption
    :param hex_strkey: Key as Hex Str
    :param hex_str_buff: Main Message as Hex Str to be encrypted
    :param algo: algo to be used
    :param hex_str_iv: iv value as Hex Str
    :return: output as hex String
    """
    encryptor = AES.new(binascii.unhexlify(hex_strkey), algo, binascii.unhexlify(hex_str_iv))
    data = encryptor.encrypt(binascii.unhexlify(hex_str_buff))
    data = data.hex().upper()
    # print('data' + data)
    return data


def generate_opc(hex_str_ki, hex_str_op):
    """
    Generate Opc using Ki and Op
    :param hex_str_ki: Ki as hex String
    :param hex_str_op: OP as hex String
    :return: hexStrOpc: OPC as hex String
    """
    hex_str_opc = aes_encrypt(hex_str_ki, hex_str_op)
    return logical_xor_(hex_str_opc, hex_str_op)


def gen_opc(ki_hex, op_hex):
    """

    :param ki_hex:
    :param op_hex:
    :return:
    """
    iv = "00000000000000000000000000000000"
    opc_hex = binascii.hexlify(AES.new(binascii.unhexlify(ki_hex), AES.MODE_CBC, IV=binascii.unhexlify(iv)).encrypt(
        binascii.unhexlify(op_hex))).decode()
    # print(opc_hex)
    return logical_xor(opc_hex, op_hex)


def sum_to_single_digit(num):
    return int(num) if (num < 10) else int(sum_to_single_digit(num / 10) + num % 10)


# Function needs to be thoroughly test
def get_luhn_digit(msg):
    """

    :param msg:
    :return:
    """
    try:
        digits = list(msg)
        odd_digits_rev = [*map(int, digits[-2::-2])]
        # even_digits_rev = [*map(int, digits[-1::-2])]
        even_digits_rev = [*map(lambda x: sum_to_single_digit(int(x) * 2), digits[-1::-2])]
        x = sum(odd_digits_rev) + sum(even_digits_rev)
        x = (10 - x % 10)
        return 0 if x == 10 else x
    except ValueError:
        return None
    except IndexError:
        return None


def validate_luhn_digit(msg):
    """
    Check if iccid last digit is with or with out Luhn Check sum digit
    :param msg:
    :return:
    """
    if not msg:
        return False
    if not ph_util.is_numeric(msg):
        return False
    last_digit = int(msg[-1])
    luhn = get_luhn_digit(msg[:-1])
    return luhn == last_digit


def append_luhn(str_plain_data, min_len_iccid_wo_luhn=18):
    return append_luhn_if_needed(str_plain_data, len(str_plain_data))


def append_luhn_if_needed(str_plain_data, min_len_iccid_wo_luhn=18):
    """
    Consider the case:
        89446172120000011  : 17 Chars, Luhn digit 4
        894461721200000114 : 18 Chars, Luhn digit 6
    :param str_plain_data:
    :param min_len_iccid_wo_luhn:
    :return:
    """
    #
    if (len(str_plain_data) == min_len_iccid_wo_luhn) or (not (validate_luhn_digit(str_plain_data))):
        # luhn has to be added, as length is minimum
        # Lugn Digit is not Present
        str_plain_data = str_plain_data + str(get_luhn_digit(str_plain_data))
    return str_plain_data


def remove_luhn_if_present(str_plain_data):
    if validate_luhn_digit(str_plain_data):  # Lugn Digit is Present
        str_plain_data = str_plain_data[0:-1]
    return str_plain_data
