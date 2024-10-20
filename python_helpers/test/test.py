import os
import unittest

import sys
import time

import python_helpers
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_crypto import PhCrypto
from python_helpers.ph_git import PhGit
from python_helpers.ph_time import PhTime
from python_helpers.ph_util import PhUtil
from python_helpers.test import test_util


def test_version():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='tool_version="1.0.1"')
    PhUtil.print_version('Test Tool', '1.0.1')
    PhUtil.print_heading(str_heading='')
    PhUtil.print_version()
    PhUtil.print_heading(str_heading='no_additional_info=True')
    PhUtil.print_version('Test Tool', '1.0.1', no_additional_info=True)
    PhUtil.print_heading(str_heading='tool_version=None')
    PhUtil.print_version('Test Tool', None)
    PhUtil.print_heading(str_heading='with_ip=True')
    PhUtil.print_version('Test Tool', '1.0.1', with_ip=True)
    PhUtil.print_heading(str_heading='with_ip=False')
    PhUtil.print_version('Test Tool', '1.0.1', with_ip=False)
    PhUtil.print_heading(str_heading='with_git_summary=True')
    PhUtil.print_version('Test Tool', '1.0.1', with_git_summary=True)
    PhUtil.print_heading(str_heading='with_git_summary=False')
    PhUtil.print_version('Test Tool', '1.0.1', with_git_summary=False)
    PhUtil.print_heading(str_heading='with_git_detailed_info=True')
    PhUtil.print_version('Test Tool', '1.0.1', with_git_detailed_info=True)
    PhUtil.print_heading(str_heading='with_git_detailed_info=False')
    PhUtil.print_version('Test Tool', '1.0.1', with_git_detailed_info=False)


def test_misc():
    PhUtil.print_heading()
    print(PhUtil.len_even('123456'))
    print(PhUtil.len_odd('123456'))


def test_list():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='cast_to_list')
    print(PhUtil.to_list(5))
    print(PhUtil.to_list('5'))
    print(PhUtil.to_list('6   ', trim_data=False))
    print(PhUtil.to_list('6   ', trim_data=True))
    print(PhUtil.to_list(['5']))
    print(PhUtil.to_list(None))
    print(PhUtil.to_list([]))
    PhUtil.print_heading(str_heading='extend_list')
    print(PhUtil.extend_list([6], 5))
    print(PhUtil.extend_list(['Pj'], 9))
    print(PhUtil.extend_list(['Pj'], 1))
    print(PhUtil.extend_list(['Pj'], 0))
    print(PhUtil.extend_list([], 5))
    print(PhUtil.extend_list(None, 5))
    print(PhUtil.extend_list(None, 5, filler='Pj'))
    print(PhUtil.extend_list(['Pj', 'Jp'], 5, filler='P'))
    PhUtil.print_heading(str_heading='extend_list, unique')
    print(PhUtil.extend_list([6], 5, unique_entries=True))
    print(PhUtil.extend_list(['Pj'], 9, unique_entries=True))
    print(PhUtil.extend_list(['Pj'], 1, unique_entries=True))
    print(PhUtil.extend_list(['Pj'], 0, unique_entries=True))
    print(PhUtil.extend_list([], 5, unique_entries=True))
    print(PhUtil.extend_list(None, 5, unique_entries=True))
    print(PhUtil.extend_list(None, 5, filler='Pj', unique_entries=True))
    print(PhUtil.extend_list(['Pj', 'Jp'], 5, filler='P', unique_entries=True))
    PhUtil.print_heading(str_heading='extend_list, unique, trim data')
    print(PhUtil.extend_list([' Pj', 'Jp '], 5, filler='P', unique_entries=True, trim_data=True))
    print(PhUtil.extend_list([' Pj', 'Jp '], 5, filler='P', unique_entries=True, trim_data=False))
    print(PhUtil.extend_list([' Pj', 'Jp '], 5, filler=' P', unique_entries=True, trim_data=True))
    print(PhUtil.extend_list([' Pj', 'Jp '], 5, filler=' P', unique_entries=True, trim_data=False))
    PhUtil.print_heading(str_heading='combine_list_items')
    print(PhUtil.combine_list_items(['Pj', 'Lp', ' nn'], trim_data=True))
    print(PhUtil.combine_list_items(['Pj', 'Lp', ' nn'], trim_data=False))
    print(PhUtil.combine_list_items('Pj'))
    PhUtil.print_heading(str_heading='combine_list_items ; clean_data=False')
    print(PhUtil.combine_list_items([';Pj ', 'Lp', 'nn'], clean_data=False))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp', 'nn'], clean_data=False))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp;', 'nn'], clean_data=False))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp;', 'nn;'], clean_data=False))
    print(PhUtil.combine_list_items(['Pj; ', '   ; Lp;', 'nn'], clean_data=False))
    print(PhUtil.combine_list_items(['P;j; ', 'Lp;', 'nn'], clean_data=False))
    print(PhUtil.combine_list_items(['# BulkMode; DirectoryInput; YmlInput; .YmlFiles;', '(3 Elements)'],
                                    clean_data=False))
    print(PhUtil.combine_list_items(['Pj;'], clean_data=False))
    print(PhUtil.combine_list_items(['Remarks semi colon 1;', 'Remarks semi colon 2; '], clean_data=False))
    print(PhUtil.combine_list_items(['Remarks semi colon 1;', 'Remarks semi colon 2; ; '], clean_data=False))
    PhUtil.print_heading(str_heading='combine_list_items ; clean_data=True')
    print(PhUtil.combine_list_items([';Pj ', 'Lp', 'nn'], clean_data=True))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp', 'nn'], clean_data=True))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp;', 'nn'], clean_data=True))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp;', 'nn;'], clean_data=True))
    print(PhUtil.combine_list_items(['Pj; ', '   ; Lp;', 'nn'], clean_data=True))
    print(PhUtil.combine_list_items(['P;j; ', 'Lp;', 'nn'], clean_data=True))
    print(PhUtil.combine_list_items(['# BulkMode; DirectoryInput; YmlInput; .YmlFiles;', '(3 Elements)'],
                                    clean_data=True))
    print(PhUtil.combine_list_items(['Pj;'], clean_data=True))
    print(PhUtil.combine_list_items(['Remarks semi colon 1;', 'Remarks semi colon 2; '], clean_data=True))
    print(PhUtil.combine_list_items(['Remarks semi colon 1;', 'Remarks semi colon 2; ; '], clean_data=True))
    print(PhUtil.combine_list_items([5, 6, 7], clean_data=True))


def test_heading():
    PhUtil.print_heading()
    PhUtil.print_heading(
        str_heading=r'..\..\Data\UserData\GSMA\SGP_22\v3_0_0\UpdateMetadataRequest\DerInput_Asn1Output_DirectInput_Asn1Element_UpdateMetadataRequest_ExportKeyword_OutputFile_export.yml')
    PhUtil.print_heading(
        str_heading='This is a long dataaaa for the testing of Trimming of remarks of individual item of the pool in asn play.; Item 100')
    PhUtil.print_heading(
        str_heading='This is a long dataaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.; Item 100')
    PhUtil.print_heading(
        str_heading='This is a long dataaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.; Item 100')
    PhUtil.print_heading(
        str_heading='This is a long dataaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.; Item 100')
    PhUtil.print_heading(
        str_heading='This is a long dataaaaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.; Item 100')


def test_python_friendly_name():
    PhUtil.print_heading()
    print(PhUtil.get_python_friendly_name(
        'Error ruamel.yaml.representer.RepresenterError: cannot represent an object: <ProfileInfoListResponse (CHOICE)>...'))
    print(PhUtil.get_python_friendly_name(
        'Error ruamel.yaml.representer.RepresenterError: cannot represent an object: <ProfileInfoListResponse (CHOICE)>...; item 1'))
    print(PhUtil.get_python_friendly_name(
        'Error ruamel.yaml.representer.RepresenterError: cannot represent an object: <ProfileInfoListResponse (CHOICE)>'))
    print(PhUtil.get_python_friendly_name('#userInput'))
    print(PhUtil.get_python_friendly_name('userInput#'))
    print(PhUtil.get_python_friendly_name('#userInput#'))


def test_remarks_append_post():
    PhUtil.print_heading()
    print(PhUtil.append_remarks('StoreMetadataRequest',
                                '..\\..\\Data\\SampleData\\GSMA\\SGP_22\\v3_0_0\\StoreMetadataRequest\\StoreMetadataRequest_wo_icon.hex'))
    print(PhUtil.append_remarks('StoreMetadataRequest',
                                '..\\..\\Data\\SampleData\\GSMA\\SGP_22\\v3_0_0\\StoreMetadataRequest\\StoreMetadataRequest_Mandatory.hex'))
    print(PhUtil.append_remarks('StoreMetadataRequest',
                                'BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202'))
    print(PhUtil.append_remarks('',
                                'StoreMetadataRequest; BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C6...'))
    print(PhUtil.append_remarks(
        'StoreMetadataRequest; BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C6...',
        ''))
    print(PhUtil.append_remarks('',
                                'BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202'))
    print(PhUtil.append_remarks(
        'BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202'))
    print(PhUtil.append_remarks('', 'item 100'))
    print(PhUtil.append_remarks('T', 'item 100'))
    print(PhUtil.append_remarks(
        'This is a long data for the testing of Trimming of remarks of individual item of the pool in asn play.',
        'item 100'))
    for i in range(1, 120):
        print(PhUtil.append_remarks(
            'a' * i + ' This is a long data for the testing of Trimming of remarks of individual item of the pool in asn play.',
            'item 100'))
        i = i + 1
    print(PhUtil.append_remarks(
        'This is a long dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
        'item 100'))


def test_remarks_append_pre():
    PhUtil.print_heading()
    print(PhUtil.append_remarks('item 100', '', append_mode_post=False))
    print(PhUtil.append_remarks('item 100', 'T', append_mode_post=False))
    print(PhUtil.append_remarks(
        'item 100',
        'This is a long data for the testing of Trimming of remarks of individual item of the pool in asn play.',
        append_mode_post=False
    ))
    for i in range(1, 120):
        print(PhUtil.append_remarks(
            'item 100',
            'a' * i + ' This is a long data for the testing of Trimming of remarks of individual item of the pool in asn play.',
            append_mode_post=False
        ))
        i = i + 1
    print(PhUtil.append_remarks(
        'item 100',
        'This is a long dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa for the testing of Trimming of remarks of individual item of the pool in asn play.',
        append_mode_post=False))
    for i in range(1, 120):
        print(PhUtil.append_remarks(
            'item 100' + '0' * i,
            ' This is a long data for the testing of Trimming of remarks of individual item of the pool in asn play.',
            append_mode_post=False
        ))
        i = i + 1


def test_temp():
    PhUtil.print_heading()


def test_hash():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='hash_algos_list')
    print(PhCrypto.hash_algos_list())
    msg = 'First'
    PhUtil.print_heading(str_heading='Str hash')
    print(f'Input String: {msg}; hash_str_sha256: {PhCrypto.hash_str_sha256(msg=msg)}')
    print(f'Input String: {msg}; hash_str: {PhCrypto.hash_str(msg=msg)}')
    print(f'Input String: {msg}; hash_str(hash_algo=sha512) {PhCrypto.hash_str(msg=msg, hash_algo="sha512")}')


def test_get_git_info():
    PhUtil.print_heading()
    PhUtil.print_heading('get_git_info_detailed; GIT_SUMMARY')
    print(f'GIT_SUMMARY: {PhGit.get_git_info_detailed(key=PhGit.KEY_GIT_SUMMARY)}')
    PhUtil.print_heading('get_git_info_detailed')
    print(PhGit.get_git_info_detailed())
    PhUtil.print_heading('get_git_info_detailed iter')
    PhUtil.print_iter(PhGit.get_git_info_detailed())


def test_get_time_stamp_file_name():
    PhUtil.print_heading()
    outputs = []
    for _ in range(15):
        data = PhUtil.get_time_stamp(files_format=True)
        print(f'{data[:13]} {data[13:15]} {data[15:]}')
    for _ in range(500):
        outputs.append(PhUtil.get_time_stamp(files_format=True))
    dup_list = [x for x in outputs if outputs.count(x) > 1]
    PhUtil.print_iter(dup_list, header='Duplicate Items')


def test_to_file():
    PhUtil.print_heading()
    PhUtil.to_file(output_lines='abc', file_name='abc.txt')
    PhUtil.to_file(output_lines='abc', file_name=os.sep.join([PhUtil.path_default_data_folder, 'abc.txt']))
    PhUtil.to_file(output_lines='abc', file_name=os.sep.join([PhUtil.path_default_data_folder, 'abc.list']))
    PhUtil.to_file(output_lines='abc', file_name=os.sep.join([PhUtil.path_default_data_folder, 'abc.ini']))
    PhUtil.to_file(output_lines=['abc', 'def', 'ghi'],
                   file_name=os.sep.join([PhUtil.path_default_data_folder, 'abc_list.txt']))
    PhUtil.to_file(output_lines='abc', back_up_file=True)
    PhUtil.to_file(output_lines='abc', file_name=os.sep.join([PhUtil.path_default_bkp_folder, 'a_b_c.txt']),
                   back_up_file=True)
    PhUtil.to_file(output_lines='abc', file_name=PhUtil.path_default_bkp_folder, back_up_file=True,
                   file_path_is_dir=True)


def test_print_iter():
    PhUtil.print_heading()
    dic1 = {
        'raw_data': '',
        'input_format': 'url',
        'remarks_list': '',
        'sample_data': 'AmenityPj',
        'sample_option': 'Load Only',
        'sample_process': '',
    }
    dic2 = {
        'app_title': '',
        'app_description': 'url',
        'app_version': '',
        'app_github_url': 'AmenityPj',
        'app_github_pages_url': 'Load Only',
    }
    dic3 = {
        '1': dic1,
        '2': dic2,
    }
    dic4 = {}
    dic5 = {'app_title': ''}
    list1 = ['raw_data', 'input_format', 'remarks_list', 'sample_data', 'sample_option', 'sample_process']
    list2 = ['app_title', 'app_description', 'app_version', 'app_github_url', 'app_github_pages_url']
    list3 = [list1, list2]
    list4 = []
    list5 = ['app_title']
    sep = PhConstants.SEPERATOR_MULTI_OBJ
    PhUtil.print_heading(str_heading='iters printing, with sep')
    PhUtil.print_iter(dic1, sep=sep)
    PhUtil.print_iter(dic2, sep=sep)
    PhUtil.print_iter(dic3, sep=sep)
    PhUtil.print_iter(dic4, sep=sep)
    PhUtil.print_iter(dic5, sep=sep)
    PhUtil.print_iter(list1, sep=sep)
    PhUtil.print_iter(list2, sep=sep)
    PhUtil.print_iter(list3, sep=sep)
    PhUtil.print_iter(list4, sep=sep)
    PhUtil.print_iter(list5, sep=sep)
    PhUtil.print_heading(str_heading='iters printing')
    PhUtil.print_iter(dic1)
    PhUtil.print_iter(dic2)
    PhUtil.print_iter(dic3)
    PhUtil.print_iter(dic4)
    PhUtil.print_iter(dic5)
    PhUtil.print_iter(list1)
    PhUtil.print_iter(list2)
    PhUtil.print_iter(list3)
    PhUtil.print_iter(list4)
    PhUtil.print_iter(list5)
    PhUtil.print_heading(str_heading='iters printing with heading')
    PhUtil.print_iter(dic1, header='dic1')
    PhUtil.print_iter(dic2, header='dic2')
    PhUtil.print_iter(dic3, header='dic3')
    PhUtil.print_iter(dic4, header='dic4')
    PhUtil.print_iter(dic5, header='dic5')
    PhUtil.print_iter(list1, header='list1')
    PhUtil.print_iter(list2, header='list2')
    PhUtil.print_iter(list3, header='list3')
    PhUtil.print_iter(list4, header='list4')
    PhUtil.print_iter(list5, header='list5')
    PhUtil.print_heading(str_heading='sys.modules; depth_level=0')
    data = sys.modules
    PhUtil.print_iter(data, depth_level=0)
    PhUtil.print_heading(str_heading='sys.modules')
    # TODO: https://pratikj.atlassian.net/browse/SML-398
    # PhUtil.print_iter(data)


def test_obj_list():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='cls_to_explore=PhUtil')
    PhUtil.get_obj_list(cls_to_explore=PhUtil, print_also=True)
    PhUtil.print_heading(str_heading="cls_to_explore=PhUtil, obj_name_filter='print'")
    PhUtil.get_obj_list(cls_to_explore=PhUtil, obj_name_filter='print', print_also=True)
    PhUtil.print_heading(str_heading='cls_to_explore=python_helpers')
    PhUtil.get_obj_list(cls_to_explore=python_helpers, print_also=True)
    PhUtil.print_heading(str_heading="cls_to_explore=python_helpers, obj_name_filter='ph'")
    PhUtil.get_obj_list(cls_to_explore=python_helpers, obj_name_filter='ph', print_also=True)


def test_get_classes_list():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='module_to_explore=python_helpers.ph_util')
    PhUtil.get_classes_list(module_to_explore=python_helpers.ph_util, print_also=True)
    PhUtil.print_heading(str_heading='module_to_explore=python_helpers.ph_util, obj_name_needed=False')
    PhUtil.get_classes_list(module_to_explore=python_helpers.ph_util, obj_name_needed=False, print_also=True)
    PhUtil.print_heading(str_heading='module_to_explore=test_util')
    PhUtil.get_classes_list(module_to_explore=test_util, print_also=True)
    PhUtil.print_heading(str_heading='module_to_explore=test_util, parent_class=unittest.TestCase')
    PhUtil.get_classes_list(module_to_explore=test_util, parent_class=unittest.TestCase, print_also=True)


def test_print_modules():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='No filter String')
    PhUtil.print_modules()
    PhUtil.print_heading(str_heading="filter_string='python_helpers'")
    PhUtil.print_modules(filter_string='python_helpers')


def test_generalise_list():
    PhUtil.print_heading()
    list1 = [1, 2, 3, 4, 5]
    PhUtil.print_iter(list1, header='list1')
    generalise_list = PhUtil.generalise_list(list1)
    PhUtil.print_iter(generalise_list, header='generalise_list')
    generalise_list_rev = PhUtil.generalise_list_reverse(generalise_list)
    PhUtil.print_iter(generalise_list_rev, header='generalise_list_rev')
    list1_rev = PhUtil.generalise_list_reverse(list1)
    PhUtil.print_iter(list1_rev, header='list1_rev')
    generalise_list_append_others = PhUtil.generalise_list(list1, append_others=True)
    PhUtil.print_iter(generalise_list_append_others, header='generalise_list_append_others')
    generalise_list_append_others_rev = PhUtil.generalise_list_reverse(generalise_list_append_others)
    PhUtil.print_iter(generalise_list_append_others_rev, header='generalise_list_append_others_rev')


def test_zipfile():
    PhUtil.print_heading()
    source_files_dir = PhUtil.path_default_data_folder
    target_dir = PhUtil.path_default_res_folder
    PhUtil.print_heading(str_heading='keep_source_dir_in_zip=True')
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir, target_dir=target_dir, keep_source_dir_in_zip=True,
                             target_file_name_wo_extn='test_zipfile_keep_source_dir_in_zip_true')
    PhUtil.print_heading(str_heading='keep_source_dir_in_zip=False')
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir, target_dir=target_dir, keep_source_dir_in_zip=False,
                             target_file_name_wo_extn='test_zipfile_keep_source_dir_in_zip_false')
    PhUtil.print_heading(str_heading='source_files_dir=target_dir')
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir, target_dir=source_files_dir,
                             target_file_name_wo_extn='test_zipfile_keep_source_path_is_dest_path')
    PhUtil.print_heading(str_heading='source_files_and_target_dir')
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir, target_dir=target_dir)
    PhUtil.print_heading(str_heading='only_source_files')
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir)
    PhUtil.print_heading(str_heading='source_dir_custom_extn_files')
    file_list = ['*.txt']
    PhUtil.zip_and_clean_dir(source_files_dir=source_files_dir, include_files=file_list,
                             target_file_name_wo_extn='test_zipfile_source_dir_custom_extn_files')


def test_chars_to_utf8():
    PhUtil.print_heading()
    target_file_name = 'test_chars_to_utf8.asn'
    lines = []
    encoding_pool = [
        PhConstants.STR_ENCODING_FORMAT_UTF8,
        PhConstants.STR_ENCODING_FORMAT_ISO_8859,
        PhConstants.STR_ENCODING_FORMAT_CP_1252,
    ]
    for encoding in encoding_pool:
        PhUtil.print_heading(f'encoding: {encoding}')
        with open(os.sep.join([PhUtil.path_default_res_folder, target_file_name]),
                  encoding=encoding, errors=None) as f:
            lines = f.readlines()
        for input_data in lines:
            output_data = PhUtil.all_chars_to_utf8(input_data)
            data = PhConstants.SEPERATOR_MULTI_LINE_TABBED.join(
                [f'input_data: {input_data}', f'output_data: {output_data}'])
            print(data)


def test_traverse_it():
    PhUtil.print_heading()
    """
    Test Data
    """
    #
    target_file_name = 'ph_bits.py'
    target_file_path = 'D:\\Other\\Github_Self\\pythonHelpers\\python_helpers\\ph_bits.py'
    target_dir_name = 'test'
    target_dir_path = 'D:\\Other\\Github_Self\\pythonHelpers\\python_helpers\\test'
    #
    src_dir_rel = os.sep.join([PhUtil.path_current_folder, os.pardir])
    src_dir = PhUtil.get_absolute_path(src_dir_rel)
    src_file_nok = target_file_path
    #
    inc_files_pattern1_ok = '*.py'
    inc_files_pattern2_ok = '*__.py'
    inc_files_pattern_nok = ['*_*.py']
    inc_files_pattern_dual_ok = ['*.py', '*.txt']
    inc_files_name_nok = target_file_name
    inc_files_name_pattern_ok = '*' + target_file_name
    #
    exc_file_name_nok = target_file_name
    exc_dir_name_nok = target_dir_name
    exc_file_path_ok = target_file_path
    exc_dir_path_ok = target_dir_path
    """
    Test Cases
    """
    #
    PhUtil.print_heading(str_heading='No Args; Working')
    PhUtil.traverse_it(print_also=True)
    #
    PhUtil.print_heading(str_heading='include_files=inc_files_pattern_dual_ok')
    PhUtil.traverse_it(print_also=True, include_files=inc_files_pattern_dual_ok)
    #
    PhUtil.print_heading(str_heading='src_dir_rel')
    PhUtil.traverse_it(print_also=True, top=src_dir_rel)
    #
    PhUtil.print_heading(str_heading='src_dir_rel, include_files=inc_files_pattern1_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir_rel, include_files=inc_files_pattern1_ok)
    #
    PhUtil.print_heading(str_heading='src_dir, include_files=inc_files_pattern1_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir, include_files=inc_files_pattern1_ok)
    #
    PhUtil.print_heading(str_heading='src_dir, include_files=inc_files_pattern2_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir, include_files=inc_files_pattern2_ok)
    #
    PhUtil.print_heading(str_heading='src_dir, include_files=inc_files_pattern_nok')
    PhUtil.traverse_it(print_also=True, top=src_dir, include_files=inc_files_pattern_nok)
    #
    PhUtil.print_heading(str_heading='src_dir, include_files=inc_files_name_nok')
    PhUtil.traverse_it(print_also=True, top=src_dir, include_files=inc_files_name_nok)
    #
    PhUtil.print_heading(str_heading='src_dir, include_files=inc_files_name_pattern_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir, include_files=inc_files_name_pattern_ok)
    #
    PhUtil.print_heading(str_heading='src_file_nok, include_files=inc_files_pattern1_ok')
    PhUtil.traverse_it(print_also=True, top=src_file_nok, include_files=inc_files_pattern1_ok)
    #
    PhUtil.print_heading(str_heading='src_file_nok')
    PhUtil.traverse_it(print_also=True, top=src_file_nok)
    #
    PhUtil.print_heading(str_heading='src_dir, excludes=exc_file_name_nok')
    PhUtil.traverse_it(print_also=True, top=src_dir, excludes=exc_file_name_nok)
    #
    PhUtil.print_heading(str_heading='src_dir, excludes=exc_dir_name_nok')
    PhUtil.traverse_it(print_also=True, top=src_dir, excludes=exc_dir_name_nok)
    #
    PhUtil.print_heading(str_heading='src_dir, excludes=exc_file_path_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir, excludes=exc_file_path_ok)
    #
    PhUtil.print_heading(str_heading='src_dir, excludes=exc_dir_path_ok')
    PhUtil.traverse_it(print_also=True, top=src_dir, excludes=exc_dir_path_ok)


def test_functions():
    test_temp()
    # Keep on the 2nd Number
    test_version()
    test_chars_to_utf8()
    test_get_git_info()
    test_get_time_stamp_file_name()
    test_to_file()
    test_misc()
    test_list()
    test_heading()
    test_python_friendly_name()
    test_remarks_append_post()
    test_remarks_append_pre()
    test_print_modules()
    test_print_iter()
    test_obj_list()
    test_get_classes_list()
    test_generalise_list()
    test_hash()
    test_zipfile()
    test_traverse_it()


def main():
    """

    :return:
    """
    """
    Time Object
    """
    ph_time = PhTime()
    ph_time.start()
    """
    Process
    """
    test_functions()
    """
    Wrap up 
    """
    ph_time.print()
    ph_time.stop()
    time.sleep(5)
    ph_time.print()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
