from src.sample import add


def test_足し算が出来る():
    # Arrange
    left = 1
    right = 2
    expected = 3
    # Act
    actual = add(left, right)
    # Assert
    assert actual == expected


def test_意図的に失敗する():
    assert False
