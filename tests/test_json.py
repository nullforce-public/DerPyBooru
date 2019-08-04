import json
import pytest
from derpibooru.image_old import ImageOld
from derpibooru.image import Image

@pytest.fixture
def json_loader():
    """Load data from a JSON file"""
    def _loader(filename):
        with open(filename, "r") as f:
            print(filename)
            data = json.load(f)
        return data
    return _loader

def test_image_is_backwards_compatible(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.id == 1

def test_image_compat(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")

    # Act
    image = ImageOld(json)

    # Assert
    assert image.id == 1
    assert image.thumb
