"""
Run Day 2 pytest tests from PyCharm.

How to use:
1. Open this file in PyCharm.
2. Right-click inside the file.
3. Click Run 'run_day2_pytest'.

It runs:
D:/Python/Python310/python.exe -m pytest ./day2_test_login_api.py -v
"""

import pytest


if __name__ == "__main__":
    exit_code = pytest.main(["day2_test_login_api.py", "-v"])
    raise SystemExit(exit_code)
