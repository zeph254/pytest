import pytest 

import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(width=10, length=5)

@pytest.fixture
def wierd_rectangle():
    return shapes.Rectangle(width=18, length=5)