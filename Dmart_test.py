import pytest
import os
from Dmart import Dmart

@pytest.fixture()
def instance():
    dmart = Dmart()
    return dmart

# Check if a file extension is .csv
def test_Extension(instance):
    if instance.data_file.lower().endswith('.csv'):
        print('Successful')

    else:
        assert False

# Check .CSV file is empty or not
def test_check(instance):
    file_path=instance.data_file
    if os.stat(file_path).st_size == 0:
        print("File is empty")
    else:
        print("File is not empity")



        




