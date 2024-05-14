import pytest

import source.shapes as shapes


def test_area(rectangle_factory):
    assert rectangle_factory(3, 2).area() == 6


def test_perimeter(rectangle_factory):
    assert rectangle_factory(3, 2).perimeter() == 5 * 2


def test_eq(rectangle_factory):
    assert rectangle_factory(3, 2) == rectangle_factory(3, 2)


def test_rect_is_not_circle(rectangle_factory):
    assert rectangle_factory(3, 2) != shapes.Circle(3)


def test_rect_is_square(square_factory):
    sq = square_factory(3)
    assert isinstance(sq, shapes.Square)
