import io
import os
import unittest.mock
from argparse import Namespace
from pathlib import PurePath

from util_helpers import util

STR_TEST_OBJ = 'test_obj :'


class test_obj_append_in_file_name:
    def __init__(self, str_file_path, str_append=None, sep=None, new_name=None, new_ext=None,
                 file_path_is_dir=None, ext_available_in_file_name=None, append_post=None,
                 expected_op=None):
        self.str_file_path = str_file_path
        self.str_append = str_append
        self.sep = sep
        self.new_name = new_name
        self.new_ext = new_ext
        self.file_path_is_dir = file_path_is_dir
        self.ext_available_in_file_name = ext_available_in_file_name
        self.append_post = append_post
        self.expected_op = expected_op


class test_obj_get_version_from_name:
    def __init__(self, name, max_depth=None, expected_op=None):
        self.name = name
        self.max_depth = max_depth
        self.expected_op = expected_op


class test_obj_normalise_name_pandas_to_user:
    def __init__(self, name, all_caps_keywords=None, expected_op=None):
        self.name = name
        self.all_caps_keywords = all_caps_keywords
        self.expected_op = expected_op


class test_obj_dec_to_hex:
    def __init__(self, dec_num, digit_required=None, even_digits=None, inbuilt=False, expected_op=None):
        self.dec_num = dec_num
        self.digit_required = digit_required
        self.even_digits = even_digits
        self.inbuilt = inbuilt
        self.expected_op = expected_op


class test_obj_hex_str_to_dec:
    def __init__(self, hex_str, expected_op=None):
        self.hex_str = hex_str
        self.expected_op = expected_op


class test_obj_hex_str_to_hex_list:
    def __init__(self, hex_str, expected_op=None):
        self.hex_str = hex_str
        self.expected_op = expected_op


class test_obj_rstrip_hex:
    def __init__(self, hex_data, expected_op=None):
        self.hex_data = hex_data
        self.expected_op = expected_op


class test_obj_analyse_data:
    def __init__(self, str_hex_data, cmt_to_print=None, print_also=None, expected_op=None):
        self.str_hex_data = str_hex_data
        self.cmt_to_print = cmt_to_print
        self.print_also = print_also
        self.expected_op = expected_op


class test_obj_print_iter:
    def __init__(self, the_iter, expected_op=None, header=None, list_as_str=None):
        self.the_iter = the_iter
        self.expected_op = expected_op
        self.header = header
        self.list_as_str = list_as_str


class test_obj_gen_isim_data:
    def __init__(self, imsi, mcc_mnc, pattern_or_data, expected_op=None):
        self.imsi = imsi
        self.mcc_mnc = mcc_mnc
        self.pattern_or_data = pattern_or_data
        self.expected_op = expected_op


class test_obj_print_seperator:
    def __init__(self, character, count, main_text, expected_op=None, tc_name=''):
        self.character = character
        self.count = count
        self.main_text = main_text
        self.expected_op = expected_op
        self.tc_name = tc_name


class test_obj_len_hex:
    def __init__(self, str_hex_data, output_in_str_format=None, expected_op=None):
        self.str_hex_data = str_hex_data
        self.output_in_str_format = output_in_str_format
        self.expected_op = expected_op


class util_test(unittest.TestCase):

    def test_appendInFileName(self):
        """
        :return:
        """
        op_file_name = 'myNameIsKhan.tmp'
        op_file_path = os.sep.join([util.path_default_out_folder, 'Youtube_PlayList.tmp'])
        src_file_path = 'D:/abc/def/123/out_file_12564.txt'
        test_obj_pool = [
            test_obj_append_in_file_name(str_file_path='temp_file.txt', str_append='pjkl',
                                         expected_op='temp_file_pjkl.txt'),
            test_obj_append_in_file_name(str_file_path=r'F:\Android\obb\com.jio.yt\temp_file.txt', str_append='pjkl',
                                         expected_op=r'F:\Android\obb\com.jio.yt\temp_file_pjkl.txt'),
            test_obj_append_in_file_name(str_file_path='temp_file.txt', str_append='pjkl', append_post=False,
                                         expected_op='pjkl_temp_file.txt'),
            test_obj_append_in_file_name(str_file_path=util.get_file_name_and_extn(
                r'F:\Android\data\com.jio.myhome.mediasharedmp\files\uploads\myNameIsKhan.txt'),
                new_ext='.tmp', expected_op=op_file_name),
            test_obj_append_in_file_name(str_file_path=util.get_file_name_and_extn(
                'F://Android//data//com.jio.myhome.mediasharedmp//files//uploads/myNameIsKhan.txt'),
                new_ext='.tmp', expected_op=op_file_name),
            test_obj_append_in_file_name(str_file_path=util.get_file_name_and_extn('myNameIsKhan.txt'),
                                         new_ext='.tmp', expected_op=op_file_name),
            test_obj_append_in_file_name(str_file_path='myNameIsKhan.txt', new_ext='.tmp', expected_op=op_file_name),
            test_obj_append_in_file_name(str_file_path='myNameIsKhan', new_ext='.tmp', expected_op=op_file_name),
            test_obj_append_in_file_name(str_file_path='target_profile', str_append=str(5 + 1),
                                         expected_op='target_profile_6'),
            test_obj_append_in_file_name(str_file_path='', str_append='pjkl', append_post=False, expected_op='pjkl'),
            test_obj_append_in_file_name(str_file_path='', str_append='pjkl', new_ext='.log', expected_op='pjkl.log'),
            test_obj_append_in_file_name(str_file_path='', str_append='', new_ext='.temp', expected_op='.temp'),
            test_obj_append_in_file_name(str_file_path='', str_append='', expected_op=''),
            test_obj_append_in_file_name(str_file_path='pjklmnop.txt', str_append=['with', 'text'],
                                         expected_op='pjklmnop_with_text.txt'),
            test_obj_append_in_file_name(str_file_path='pjklmnop.txt', str_append=['output', 'data', '20210721'],
                                         new_ext='.out', expected_op='pjklmnop_output_data_20210721.out'),
            test_obj_append_in_file_name(
                str_file_path=os.sep.join([util.path_default_tst_folder, 'prog', 'raw', 'prog']), new_ext='.txt',
                expected_op= os.sep.join([util.path_default_tst_folder, 'prog', 'raw', 'prog.txt'])),
            test_obj_append_in_file_name(
                str_file_path=os.sep.join([util.path_default_out_folder, 'names_Generated']),
                str_append='fileNameKeyword', new_ext='.txt',
                expected_op=os.sep.join([util.path_default_out_folder, 'names_Generated_fileNameKeyword.txt'])),
            test_obj_append_in_file_name(
                str_file_path=os.sep.join([util.path_default_out_folder, 'names_Generated.asn']),
                str_append='fileNameKeyword', new_ext='.txt',
                expected_op=os.sep.join([util.path_default_out_folder, 'names_Generated_fileNameKeyword.txt'])),
            test_obj_append_in_file_name(
                str_file_path='names_Generated.asn', str_append='fileNameKeyword', new_ext='.txt',
                expected_op='names_Generated_fileNameKeyword.txt'),
            test_obj_append_in_file_name(str_file_path='PROFILE_OPERATIONAL1.8.35.txt', str_append='1',
                                         expected_op='PROFILE_OPERATIONAL1.8.35_1.txt'),
            test_obj_append_in_file_name(str_file_path='PROFILE_OPERATIONAL1.8.35.txt', str_append='1',
                                         sep='.', expected_op='PROFILE_OPERATIONAL1.8.35.1.txt'),
            test_obj_append_in_file_name(str_file_path='profile_name', str_append=['profile_data', 'extra_keyword'],
                                         new_ext='.txt', ext_available_in_file_name=False,
                                         expected_op='profile_name_profile_data_extra_keyword.txt'),
            test_obj_append_in_file_name(str_file_path='PROFILE_OPERATIONAL1.8.35',
                                         str_append=['profile_data'],
                                         new_ext='.txt', ext_available_in_file_name=False,
                                         expected_op='PROFILE_OPERATIONAL1.8.35_profile_data.txt'),
            test_obj_append_in_file_name(str_file_path='PROFILE_OPERATIONAL1.8.35',
                                         str_append=['profile_data'],
                                         new_ext='.txt', expected_op='PROFILE_OPERATIONAL1.8_profile_data.txt'),
            test_obj_append_in_file_name(str_file_path=src_file_path, new_ext='.out', new_name='123456',
                                         expected_op='D:/abc/def/123/123456.out'),
            test_obj_append_in_file_name(str_file_path=src_file_path, new_name='123456',
                                         expected_op='D:/abc/def/123/123456.txt'),
            test_obj_append_in_file_name(
                str_file_path=util.get_file_name_and_extn(src_file_path,
                                                          only_path=True) + os.sep + '_file_name', new_ext='.asn',
                expected_op='D:/abc/def/123/\_file_name.asn'),
            test_obj_append_in_file_name(str_file_path=os.sep.join(
                [util.get_file_name_and_extn(src_file_path, only_path=True),
                 '_file_name']), new_ext='.asn', expected_op='D:/abc/def/123/\_file_name.asn'),
            test_obj_append_in_file_name(str_file_path=src_file_path, str_append=PurePath(src_file_path).parent.name,
                                         new_ext='.asn',
                                         expected_op='D:/abc/def/123/out_file_12564_123.asn'),
            test_obj_append_in_file_name(
                str_file_path=util.path_default_out_folder, str_append=['Youtube', 'PlayList'], new_ext='.tmp',
                expected_op=util.path_default_out_folder + '_Youtube_PlayList.tmp'),
            test_obj_append_in_file_name(
                str_file_path=util.path_default_out_folder + os.sep, str_append=['Youtube', 'PlayList'],
                new_ext='.tmp', file_path_is_dir=True, expected_op=op_file_path),
            test_obj_append_in_file_name(
                str_file_path=util.path_default_out_folder + os.sep, str_append=['Youtube', 'PlayList'],
                new_ext='.tmp', expected_op=op_file_path),
            test_obj_append_in_file_name(
                str_file_path=os.sep.join([util.path_default_out_folder, '']), str_append=['Youtube', 'PlayList'],
                new_ext='.tmp', expected_op=op_file_path),
            test_obj_append_in_file_name(
                str_file_path=os.sep.join([util.path_default_out_folder, '']), new_name='dest_vs_block',
                new_ext='.txt', expected_op=os.sep.join([util.path_default_out_folder, 'dest_vs_block.txt'])),
        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(
                    util.append_in_file_name(str_file_path=test_obj.str_file_path, str_append=test_obj.str_append,
                                             sep=test_obj.sep, new_name=test_obj.new_name, new_ext=test_obj.new_ext,
                                             file_path_is_dir=test_obj.file_path_is_dir,
                                             ext_available_in_file_name=test_obj.ext_available_in_file_name,
                                             append_post=test_obj.append_post), test_obj.expected_op)

    def test_get_version_from_name(self):
        """
        :return:
        """
        test_obj_pool = [
            test_obj_get_version_from_name(name='SGP.22-v2.0.pdf', max_depth=None, expected_op='v2_0'),
            test_obj_get_version_from_name(name='SGP.22-v2.0.txt', max_depth=None, expected_op='v2_0'),
            test_obj_get_version_from_name(name='SGP.22-v2.2.1-2.txt', max_depth=None, expected_op='v2_2_1_2'),
            test_obj_get_version_from_name(name='SGP.22-v2.2.1-2.txt', max_depth=3, expected_op='v2_2_1'),
            test_obj_get_version_from_name(name='SGP.22-v2.2.2.txt', max_depth=None, expected_op='v2_2_2'),
            test_obj_get_version_from_name(name='SGP.22_v1.0.txt', max_depth=None, expected_op='v1_0'),
            test_obj_get_version_from_name(name='SGP.22_v2.2.txt', max_depth=None, expected_op='v2_2'),
            test_obj_get_version_from_name(name='SGP.22_v2.0-Technical_Specification-eSIMRSP.pdf', max_depth=None,
                                           expected_op='v2_0'),
            test_obj_get_version_from_name(name='SGP.22_v2.0-Technical Specification-eSIMRSP.pdf', max_depth=None,
                                           expected_op='v2_0'),
        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(
                    util.get_version_from_name(test_obj.name, max_depth=test_obj.max_depth),
                    test_obj.expected_op)

    def test_normalise_name_pandas_to_user(self):

        """
        :return:
        """

        test_obj_pool = [
            test_obj_normalise_name_pandas_to_user(name='ICCID', expected_op='ICCID'),
            test_obj_normalise_name_pandas_to_user(name='IMSI', expected_op='IMSI'),
            test_obj_normalise_name_pandas_to_user(name='MATCHING_ID', expected_op='Matching ID'),
            test_obj_normalise_name_pandas_to_user(name='MSISDN', expected_op='MSISDN'),
            test_obj_normalise_name_pandas_to_user(name='CONFIRMATION_CODE', all_caps_keywords=['CODE'],
                                                   expected_op='Confirmation CODE'),
            test_obj_normalise_name_pandas_to_user(name='CONFIRMATION_CODE', all_caps_keywords=['CONFIRMATION', 'CODE'],
                                                   expected_op='CONFIRMATION CODE'),
            test_obj_normalise_name_pandas_to_user(name='CONFIRMATION_CODE', expected_op='Confirmation Code'),
        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(util.normalise_name_pandas_to_user(test_obj.name, test_obj.all_caps_keywords),
                                 test_obj.expected_op)

    def test_dec_to_hex(self):
        """

        :return:
        """
        test_obj_pool = [
            test_obj_dec_to_hex(15, expected_op='0F'),
            test_obj_dec_to_hex(15, expected_op='0F', even_digits=True),
            test_obj_dec_to_hex(15, expected_op='F', even_digits=False),
            test_obj_dec_to_hex(16, expected_op='10'),
            test_obj_dec_to_hex(16, expected_op='10', even_digits=True),
            test_obj_dec_to_hex(16, expected_op='10', even_digits=False),
            test_obj_dec_to_hex(15, digit_required=32, expected_op='0000000000000000000000000000000F'),
            test_obj_dec_to_hex(16, digit_required=32, expected_op='00000000000000000000000000000010'),
            test_obj_dec_to_hex(15, expected_op='0xf', inbuilt=True),
            test_obj_dec_to_hex(16, expected_op='0x10', inbuilt=True),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                if test_obj.inbuilt:
                    self.assertEqual(hex(test_obj.dec_num), test_obj.expected_op)
                    continue
                if test_obj.digit_required is not None:
                    self.assertEqual(util.dec_to_hex(test_obj.dec_num, test_obj.digit_required),
                                     test_obj.expected_op)
                else:
                    if test_obj.even_digits is not None:
                        self.assertEqual(util.dec_to_hex(test_obj.dec_num, test_obj.digit_required,
                                                         even_digits=test_obj.even_digits),
                                         test_obj.expected_op)
                    else:
                        self.assertEqual(util.dec_to_hex(test_obj.dec_num), test_obj.expected_op)

    def test_hex_str_to_dec(self):
        """

        :return:
        """
        test_obj_pool = [
            test_obj_hex_str_to_dec('fff', expected_op=4095),
            test_obj_hex_str_to_dec('0fff', expected_op=4095),
            test_obj_hex_str_to_dec('FFF', expected_op=4095),
            test_obj_hex_str_to_dec('0xfff', expected_op=4095),
            test_obj_hex_str_to_dec('10', expected_op=16),
            test_obj_hex_str_to_dec('0x10', expected_op=16),
            test_obj_hex_str_to_dec('0x0A', expected_op=10),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(util.hex_str_to_dec(test_obj.hex_str), test_obj.expected_op)

    def test_hex_str_to_hex_list(self):
        """

        :return:
        """
        test_obj_pool = [
            test_obj_hex_str_to_hex_list('A000000559 1010 FFFFFF FF89 000001 00',
                                         expected_op=[160, 0, 0, 5, 89, 16, 16, 255, 255, 255, 255, 137, 0, 0, 1, 0]),
            test_obj_hex_str_to_hex_list('A000000559 1010 FFFFFF FF89 000001 0',
                                         expected_op=[160, 0, 0, 5, 89, 16, 16, 255, 255, 255, 255, 137, 0, 0, 1, 0]),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(util.hex_str_to_hex_list(test_obj.hex_str), test_obj.expected_op)

    def test_rstrip_hex(self):
        """

        :return:
        """
        test_obj_pool = [
            test_obj_rstrip_hex('37F08037F010FFFFFFFFFFFF', expected_op='37F08037F010'),
            test_obj_rstrip_hex('37F08037F010FFFFFFFFFFF', expected_op='37F08037F010F'),
            test_obj_rstrip_hex(
                '37F030800037F020800037F030008037F0200080270243808017F671808027F420808027F430808027F44080801300148080371211808037F630808012F440808047F810808047F020808022F210808002F802808032F4028080330450808017F410808035F050808047F440808017F210808002F602808007F420808005F281808015F0988080FFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0F',
                expected_op='37F030800037F020800037F030008037F0200080270243808017F671808027F420808027F430808027F44080801300148080371211808037F630808012F440808047F810808047F020808022F210808002F802808032F4028080330450808017F410808035F050808047F440808017F210808002F602808007F420808005F281808015F0988080FFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0FFFFFFF3F0F'),
            test_obj_rstrip_hex('61184F10A0000000871002FF33FF01890000010050045553494DFFFFFFFFFFFFFFFFFFFFFFFF',
                                expected_op='61184F10A0000000871002FF33FF01890000010050045553494D'),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(util.rstrip_hex_str(test_obj.hex_data), test_obj.expected_op)

    def test_analyse_data(self):
        """

        :return:
        """
        test_obj_pool = [
            test_obj_analyse_data('123456', expected_op='Length: 6 digits(s) / 03 byte(s), Data: 123456'),
            test_obj_analyse_data('12345', expected_op='Odd Length, Length: 5 digits(s) / 02 byte(s), Data: 12345'),
            test_obj_analyse_data('123456', cmt_to_print='1st',
                                  expected_op='\n1st\t:Length: 6 digits(s) / 03 byte(s), Data: 123456'),
            test_obj_analyse_data('12345', cmt_to_print='2nd',
                                  expected_op='\n2nd\t:Odd Length, Length: 5 digits(s) / 02 byte(s), Data: 12345'),
            test_obj_analyse_data('123456', cmt_to_print='1st', print_also=True,
                                  expected_op='\n1st\t:Length: 6 digits(s) / 03 byte(s), Data: 123456'),
            test_obj_analyse_data('12345', cmt_to_print='2nd', print_also=True,
                                  expected_op='\n2nd\t:Odd Length, Length: 5 digits(s) / 02 byte(s), Data: 12345'),
            test_obj_analyse_data('0123456789', cmt_to_print='3rd', print_also=True,
                                  expected_op='\n3rd\t:Length: 10 digits(s) / 05 byte(s), Data: 0123456789'),
            test_obj_analyse_data('01234567890', cmt_to_print='3rd', print_also=True,
                                  expected_op='\n3rd\t:Odd Length, Length: 11 digits(s) / 05 byte(s), Data: 01234567890'),
            test_obj_analyse_data('01234567890123456789', cmt_to_print='4th', print_also=True,
                                  expected_op='\n4th\t:Length: 20 digits(s) / 0A byte(s), Data: 01234567890123456789'),
            test_obj_analyse_data('012345678901234567890', cmt_to_print='4th', print_also=True,
                                  expected_op='\n4th\t:Odd Length, Length: 21 digits(s) / 0A byte(s), Data: 012345678901234567890'),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                if test_obj.cmt_to_print and test_obj.print_also:
                    self.assertEqual(util.analyse_data(test_obj.str_hex_data, test_obj.cmt_to_print,
                                                       test_obj.print_also), test_obj.expected_op)
                elif test_obj.cmt_to_print:
                    self.assertEqual(util.analyse_data(test_obj.str_hex_data, test_obj.cmt_to_print),
                                     test_obj.expected_op)
                else:
                    self.assertEqual(util.analyse_data(test_obj.str_hex_data), test_obj.expected_op)

    def test_print_iter(self):
        dict_1 = {'pre_defined_script': 'cmds_esim_ara_m_select',
                  'pre_defined_script_multi': None,
                  'custom_script': '',
                  'iccid': '89111100000000000008',
                  'imsi': '222013000000000',
                  'aid_usim': 'A0000000871002FF33FF018900000100',
                  'aid_isim': 'A0000000871004FF33FF018900000100',
                  'param_gen_1': None,
                  'param_gen_2': '',
                  'auto_fetch': 'True',
                  'auto_get_response': 'True',
                  'auto_cmd_for_6cxx': 'True',
                  'log_mode_append': 'True',
                  'help_mode': 'False',
                  'virtual_card': 'False'}
        dict_1_print = f'pre_defined_script: cmds_esim_ara_m_select\n' \
                       f'pre_defined_script_multi: None\n' \
                       f'custom_script: \n' \
                       f'iccid: 89111100000000000008\n' \
                       f'imsi: 222013000000000\n' \
                       f'aid_usim: A0000000871002FF33FF018900000100\n' \
                       f'aid_isim: A0000000871004FF33FF018900000100\n' \
                       f'param_gen_1: None\n' \
                       f'param_gen_2: \n' \
                       f'auto_fetch: True\n' \
                       f'auto_get_response: True\n' \
                       f'auto_cmd_for_6cxx: True\n' \
                       f'log_mode_append: True\n' \
                       f'help_mode: False\n' \
                       f'virtual_card: False\n'
        list_1 = ['F9526EFF9CAE23D00C77860F9BAEB301', '554B60ACA30428BF920918F16D102218',
                  '237CC88B687C5C97F9FD9A504BD7BB4C', '408FE089A8665EFC3419EF20277C2020',
                  '4DD24459B14E1E8A71C17578854A94EB', '3A0FD2809DAE5A7E884D0B22FFFA6134',
                  'FEF2A8D1E05CF65B4A61CC3BF05F5395', '4DD7419D2AFB3D44DC19BF0D344F36AC',
                  'D241FD541C09A30E87429E42CB8C66BA', '22FB24FF6D553A0A5589B171A2EAB725']
        list_1_print = f'F9526EFF9CAE23D00C77860F9BAEB301\n' \
                       f'554B60ACA30428BF920918F16D102218\n' \
                       f'237CC88B687C5C97F9FD9A504BD7BB4C\n' \
                       f'408FE089A8665EFC3419EF20277C2020\n' \
                       f'4DD24459B14E1E8A71C17578854A94EB\n' \
                       f'3A0FD2809DAE5A7E884D0B22FFFA6134\n' \
                       f'FEF2A8D1E05CF65B4A61CC3BF05F5395\n' \
                       f'4DD7419D2AFB3D44DC19BF0D344F36AC\n' \
                       f'D241FD541C09A30E87429E42CB8C66BA\n' \
                       f'22FB24FF6D553A0A5589B171A2EAB725\n'
        list_1_str_print = f"[" \
                           f"'F9526EFF9CAE23D00C77860F9BAEB301', " \
                           f"'554B60ACA30428BF920918F16D102218', " \
                           f"'237CC88B687C5C97F9FD9A504BD7BB4C', " \
                           f"'408FE089A8665EFC3419EF20277C2020', " \
                           f"'4DD24459B14E1E8A71C17578854A94EB', " \
                           f"'3A0FD2809DAE5A7E884D0B22FFFA6134', " \
                           f"'FEF2A8D1E05CF65B4A61CC3BF05F5395', " \
                           f"'4DD7419D2AFB3D44DC19BF0D344F36AC', " \
                           f"'D241FD541C09A30E87429E42CB8C66BA', " \
                           f"'22FB24FF6D553A0A5589B171A2EAB725'" \
                           f"]\n"
        list_1_str_print_header = 'List as Str'
        header_joiner = ': '
        test_obj_pool = [
            test_obj_print_iter('37F08037F010FFFFFFFFFFFF', expected_op='37F08037F010FFFFFFFFFFFF\n'),
            test_obj_print_iter(123, expected_op='123\n'),
            test_obj_print_iter(123.09, expected_op='123.09\n'),
            test_obj_print_iter(dict_1, expected_op=dict_1_print),
            test_obj_print_iter(Namespace(**dict_1), expected_op=dict_1_print),
            test_obj_print_iter(list_1, expected_op=list_1_print),
            test_obj_print_iter(list_1, expected_op=list_1_str_print, list_as_str=True),
            test_obj_print_iter(list_1, expected_op=header_joiner.join([list_1_str_print_header, list_1_str_print]),
                                header=list_1_str_print_header, list_as_str=True),
        ]

        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assert_stdout_print_iter(test_obj)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_print_iter(self, test_obj, mock_stdout):
        self.maxDiff = None
        util.print_iter(the_iter=test_obj.the_iter, list_as_str=test_obj.list_as_str, header=test_obj.header)
        actual_value = mock_stdout.getvalue()
        expected_value = test_obj.expected_op
        self.assertEqual(actual_value, expected_value)

    def test_len_hex(self):
        """
        :return:
        """
        test_obj_pool = [
            test_obj_len_hex(str_hex_data='123456', output_in_str_format=True, expected_op='03'),
            test_obj_len_hex(str_hex_data='123456', output_in_str_format=False, expected_op=3),
            test_obj_len_hex(str_hex_data='123456', expected_op=3),
            test_obj_len_hex(str_hex_data='01234567890123456789', output_in_str_format=True, expected_op='0A'),
            test_obj_len_hex(str_hex_data='01234567890123456789', output_in_str_format=False, expected_op=0x0A),
            test_obj_len_hex(str_hex_data='01234567890123456789', expected_op=0x0A),

        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                if test_obj.output_in_str_format:
                    self.assertEqual(
                        util.len_hex(str_hex_data=test_obj.str_hex_data,
                                     output_in_str_format=test_obj.output_in_str_format),
                        test_obj.expected_op)
                else:
                    self.assertEqual(
                        util.len_hex(str_hex_data=test_obj.str_hex_data),
                        test_obj.expected_op)

    def test_gen_isim_data(self):
        """
        :return:
        """
        test_obj_pool = [
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='23450',
                                   pattern_or_data='ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='ims.mnc050.mcc234.3gppnetwork.org'),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='234507',
                                   pattern_or_data='ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='ims.mnc507.mcc234.3gppnetwork.org'),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='23450',
                                   pattern_or_data='${IMSI}@ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='234507095401016@ims.mnc050.mcc234.3gppnetwork.org'),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='234507',
                                   pattern_or_data='${IMSI}@ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='234507095401016@ims.mnc507.mcc234.3gppnetwork.org', ),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='23450',
                                   pattern_or_data='sip:${IMSI}@ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='sip:234507095401016@ims.mnc050.mcc234.3gppnetwork.org'),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='234507',
                                   pattern_or_data='sip:${IMSI}@ims.mnc${MNC}.mcc${MCC}.3gppnetwork.org',
                                   expected_op='sip:234507095401016@ims.mnc507.mcc234.3gppnetwork.org'),
            test_obj_gen_isim_data(imsi='234507095401016', mcc_mnc='23450',
                                   pattern_or_data='pratik.jaiswal@montymobile.com',
                                   expected_op='pratik.jaiswal@montymobile.com'),
        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + str(count)):
                self.assertEqual(
                    util.gen_isim_data(imsi=test_obj.imsi, mcc_mnc=test_obj.mcc_mnc,
                                       pattern_or_data=test_obj.pattern_or_data),
                    test_obj.expected_op)

    def test_print_separator(self):
        """
              :return:
              """
        test_obj_pool = [
            test_obj_print_seperator(
                character='-', count=80,
                main_text='0',
                expected_op='--------------------------------------- 0 ---------------------------------------',
                tc_name='1 char (Odd)'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='01',
                expected_op='--------------------------------------- 01 ---------------------------------------',
                tc_name='2 char (Even)'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='01234567890123456',
                expected_op='------------------------------- 01234567890123456 -------------------------------',
                tc_name='Odd chars'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='0123456789012345',
                expected_op='-------------------------------- 0123456789012345 --------------------------------',
                tc_name='Even chars'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='01234567890123456789012345678901234567890123456789012345678901234567890123456789',
                expected_op='- 01234567890123456789012345678901234567890123456789012345678901234567890123456789 -',
                tc_name='chars same as count'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='012345678901234567890123456789012345678901234567890123456789012345678901234567',
                expected_op='- 012345678901234567890123456789012345678901234567890123456789012345678901234567 -',
                tc_name='chars = count -2 '),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='0123456789012345678901234567890123456789012345678901234567890123456789012345',
                expected_op='- 0123456789012345678901234567890123456789012345678901234567890123456789012345 -',
                tc_name='chars = count -4'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text=None,
                expected_op='--------------------------------------------------------------------------------',
                tc_name='main_text is None'),
            test_obj_print_seperator(
                character='-', count=80,
                main_text='-',
                expected_op='--------------------------------------- - ---------------------------------------'),
        ]
        for count, test_obj in enumerate(test_obj_pool, start=1):
            tc_name = test_obj.tc_name if test_obj.tc_name else str(count)
            with self.subTest(STR_TEST_OBJ + tc_name):
                self.assertEqual(
                    util.print_separator(character=test_obj.character, count=test_obj.count,
                                         main_text=test_obj.main_text, get_only=True)
                    , test_obj.expected_op)


if __name__ == '__main__':
    unittest.main()
