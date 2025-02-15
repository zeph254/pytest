import pytest

import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area ", [(1, 1), (2, 4), (3, 9)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area



    

@pytest.mark.parametrize("side_length, expected_perimeter", [(1, 4), (2, 8), (3, 12)]) 
def test_multiple_permeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter   

