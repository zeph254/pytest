import pytest

import source.shapes as shapes



def test_area(my_rectangle):

    # rectangle = shapes.Rectangle(width=10, length=5)

    assert my_rectangle.area() == 10*5

def test_perimeter(my_rectangle):    
    # rectangle = shapes.Rectangle(width=10, length=5)

    assert my_rectangle.perimeter() == 2*(10+5)


def test_not_equal(my_rectangle, wierd_rectangle):
    assert my_rectangle != wierd_rectangle    