from python_helpers.ph_util import PhUtil


def test_version():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='')
    PhUtil.print_version('Test Tool', '1.0.1')
    PhUtil.print_heading(str_heading='')
    PhUtil.print_version()
    PhUtil.print_heading(str_heading='')
    PhUtil.print_version('Test Tool', '1.0.1', no_additional_info=True)


def test_misc():
    PhUtil.print_heading()
    print(PhUtil.len_even('123456'))
    print(PhUtil.len_odd('123456'))


def test_list():
    PhUtil.print_heading()
    PhUtil.print_heading(str_heading='cast_to_list')
    print(PhUtil.cast_to_list(5))
    print(PhUtil.cast_to_list('5'))
    print(PhUtil.cast_to_list('6   ', trim_data=False))
    print(PhUtil.cast_to_list('6   ', trim_data=True))
    print(PhUtil.cast_to_list(['5']))
    print(PhUtil.cast_to_list(None))
    print(PhUtil.cast_to_list([]))
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
    # print(PhUtil.combine_list_items(['Pj;'], clean_data=True))
    pass


def main():
    test_temp()
    test_version()
    test_misc()
    test_list()
    test_heading()
    test_python_friendly_name()
    test_remarks_append_post()
    test_remarks_append_pre()


if __name__ == '__main__':
    main()
