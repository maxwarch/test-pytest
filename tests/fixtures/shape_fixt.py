import pytest

import source.shapes as shapes


@pytest.fixture
def rect():
    return shapes.Rectangle(2, 3)


@pytest.fixture
def square():
    return shapes.Rectangle(2, 2)


@pytest.fixture
def rectangle_factory():
    def create_rectangle(width, height=0, is_square=False):
        return (
            shapes.Rectangle(width, width)
            if is_square
            else shapes.Rectangle(width, height)
        )

    return create_rectangle


@pytest.fixture
def square_factory():
    def create_square(width):
        return shapes.Square(width)

    return create_square
