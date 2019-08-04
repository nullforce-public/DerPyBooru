"""Test Image class json parsing"""
import json
import pytest
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

def test_json_loading(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json_str = json_loader("tests/2108665.json")

    # Act
    image = Image(json_str)

    # Assert
    assert image.data

def test_image_json_is_not_image(json_loader):
    """Test that image_json is not image"""
    # Arrange
    json_str = json_loader("tests/2108665.json")

    # Act
    image = Image(json_str)

    # Assert
    assert image.image != image.image_json
