"""
Tests backwards compatibility of the Image class introduced in v1 with the
original Image class in v0.
"""
import json
import pytest
from derpibooru.image_old import ImageOld
from derpibooru.image import Image

# pylint: disable=redefined-outer-name

@pytest.fixture
def json_loader():
    """Load data from a JSON file"""
    def _loader(filename):
        with open(filename, "r") as f:
            print(filename)
            data = json.load(f)
        return data
    return _loader

# def test_image_has_comments(json_loader):
#     """
#     Tests whether the results in a query contain the tag that was being searched
#     for
#     """
#     # Arrange
#     json = json_loader("tests/1.json")

#     # Act
#     image = Image.from_dict(json)

#     # Assert
#     assert image.comments

def test_image_has_data(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.data

# def test_image_has_faved_by(json_loader):
#     """
#     Tests whether the results in a query contain the tag that was being searched
#     for
#     """
#     # Arrange
#     json = json_loader("tests/1.json")

#     # Act
#     image = Image.from_dict(json)

#     # Assert
#     assert image.faved_by

def test_image_has_full(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.full == image_old.full

def test_image_has_large(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.large == image_old.large

def test_image_has_medium(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.medium == image_old.medium

def test_image_has_small(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.small == image_old.small

def test_image_has_tags(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.tags == image_old.tags

def test_image_has_tall(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.tall == image_old.tall

def test_image_has_thumb(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.thumb == image_old.thumb

def test_image_has_thumb_tiny(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.thumb_tiny == image_old.thumb_tiny

def test_image_has_thumb_small(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.thumb_small == image_old.thumb_small

def test_image_has_url(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.url == image_old.url

def test_image_has_fields(json_loader):
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
    assert image.representations
    assert image.image

def test_image_breaking_changes(json_loader):
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    # Arrange
    json = json_loader("tests/1.json")
    image_old = ImageOld(json)

    # Act
    image = Image.from_dict(json)

    # Assert
    assert image.id == 1
    # pylint: disable=no-member
    # dates were strings but are datetime now
    assert image.created_at != image_old.created_at
    assert image.updated_at != image_old.updated_at
    assert image.first_seen_at != image_old.first_seen_at
    # assert image.comments == image_old.comments
