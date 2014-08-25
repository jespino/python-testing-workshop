import os
from unittest import mock

with mock.patch('os.getcwd'):
    os.getcwd.return_value = "test"
    print(os.getcwd())

print(os.getcwd())
