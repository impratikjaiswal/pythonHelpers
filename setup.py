# -*- coding: UTF−8 -*-

import os

from setuptools import setup, find_packages
from python_helpers._tool_name import TOOL_NAME

# all packages dependencies
packages = find_packages()
if not packages:
    print(f'Selecting Hardcoded Packages')
    packages = [
        "python_helpers",
    ]
print(f'Packages are {packages}')
# potential dependencies
install_reqs = [
    'packaging',
    'pandas',
    'psutil',
    'tzlocal',
    'incremental',
    'requests',
]

setup_reqs = [
    'incremental',
]

# get long description from the README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    use_incremental=True,
    setup_requires=setup_reqs,
    name=TOOL_NAME,
    author="Pratik Jaiswal",
    author_email="impratikjaiswal@gmail.com",
    description="A Python software package suite to provide various utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/impratikjaiswal/pythonHelpers",
    project_urls={
        "Bug Tracker": "https://github.com/impratikjaiswal/pythonHelpers",
    },
    keywords="Common Functions Funcs Util Utility",
    license="MIT",
    python_requires=">=3.9",
    packages=packages,
    install_requires=install_reqs
    # test_suite="test.sample_package",
)
