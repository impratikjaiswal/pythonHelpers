from python_helpers.ph_util import PhUtil

SEPERATOR = """echo.
echo.
echo.
echo.
echo "XXX"
"""


class PhDos:

    @classmethod
    def delete_file(cls, target_file_path, conditional=True):
        del_cmd = f'DEL /F /S /Q /A "{target_file_path}"'
        return f'if exist "{target_file_path}" {del_cmd}' if conditional else del_cmd

    @classmethod
    def delete_empty_dirs_in_current_folder(cls):
        return 'for /f "delims=" %%d in (\'dir /s /b /ad ^| sort /r\') do rd "%%d"'

    @classmethod
    def create_zip_file(cls, target_zip, source_files):
        return f'7z a -t7z -sdel "{target_zip}" "{source_files}"'

    @classmethod
    def switch_to_current_folder(cls):
        return 'pushd %~dp0'

    @classmethod
    def echo_off(cls):
        return '@echo off'

    @classmethod
    def get_seperator(cls, heading=None):
        heading = PhUtil.set_if_not_empty(heading, '---------------')
        return SEPERATOR.replace('XXX', heading)

    @classmethod
    def comment_line(cls, line=None):
        return f'REM {line}'
