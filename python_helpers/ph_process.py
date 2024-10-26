import os
import subprocess

from python_helpers.ph_constants import PhConstants


class PhProcess:
    """
    Alternatives: https://pypi.org/project/python-git-info/
    """

    @classmethod
    def execute_command_in_shell(cls, cmd, cwd=None, decode_mode=PhConstants.STR_ENCODING_FORMAT_UTF8, strip_data=True,
                                 fail_safe=False):
        try:
            result = subprocess.check_output(cmd, cwd=cwd)
            if decode_mode:
                result = result.decode(decode_mode)
            if strip_data:
                result = result.strip()
            return result
        except subprocess.CalledProcessError as e:
            if fail_safe is True:
                return None
            raise e
        except Exception as e:
            if fail_safe is True:
                return None
            raise e

    @classmethod
    def open_file(cls, file_path):
        print(f'Opening {file_path}')
        subprocess.Popen([file_path], shell=True)

    @classmethod
    def run_batch_file(cls, batch_file_path):
        """
        Run a batch file

        :param batch_file_path:
        :return:
        """
        batch_file_path = f'"{batch_file_path}"'
        print(f'Executing {batch_file_path}')
        os.system(batch_file_path)
        # https://pratikj.atlassian.net/browse/SML-409; Delay did not work
        # time.sleep(2)
