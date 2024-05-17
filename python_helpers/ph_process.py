import subprocess

from python_helpers.ph_constants import PhConstants


class PhProcess:
    """
    Alternatives: https://pypi.org/project/python-git-info/
    """

    @classmethod
    def execute_command_in_shell(cls, cmd, cwd=None, decode_mode=PhConstants.DECODE_MODE_UTF8, strip_data=True,
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
