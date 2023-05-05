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
    print(PhUtil.cast_to_list('6   '))
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
    print(PhUtil.extend_list([' Pj', 'Jp '], 5, filler=' P', unique_entries=True, trim_data=True))
    PhUtil.print_heading(str_heading='combine_list_items')
    print(PhUtil.combine_list_items(['Pj', 'Lp', 'nn']))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp', 'nn']))
    print(PhUtil.combine_list_items(['Pj; ', 'Lp;', 'nn']))
    print(PhUtil.combine_list_items(['Pj; ', '   ; Lp;', 'nn']))
    print(PhUtil.combine_list_items(['Pj;']))



def test_heading():
    PhUtil.print_heading()


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


def main():
    test_version()
    test_misc()
    test_list()
    test_heading()
    test_python_friendly_name()


if __name__ == '__main__':
    main()
