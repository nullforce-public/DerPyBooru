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
    """Test JSON to Image"""
    # Arrange
    json_str = json_loader("tests/1384692_philomena.json")

    # Act
    image = Image(json_str["image"])

    # Assert
    assert image.data
    assert image.aspect_ratio == 0.7588075880758808
    assert image.comment_count == 32
    assert image.created_at == "2017-03-11T20:32:14"
    assert image.deletion_reason == None
    assert image.description == "Pony in box, inspired by my cat as usual X3 Just quick color sketch)"
    assert image.downvotes == 6
    assert image.duplicate_of == None
    assert image.faves == 1408
    assert image.first_seen_at == "2017-03-11T20:32:14"
    assert image.format == "PNG"
    assert image.height == 1845
    assert image.hidden_from_users == False
    assert image.id == 1384692
    assert image.intensities
    assert image.intensities["ne"] == 47.18749482864885
    assert image.intensities["nw"] == 34.67088259646406
    assert image.intensities["se"] == 50.750106697638415
    assert image.intensities["sw"] == 30.735388683030067
    assert image.mime_type == "image/png"
    assert image.name == "favorite_place__color_sketch__by_yakovlev_vad-db1ybkb.png"
    assert image.orig_sha512_hash == "a5b68e1cb435a818cc15d5a4e8f879d350700ae1dbe9d12b7d9e421abc6d2f6b622318d99d0e5b120c2c59b3df3b9b120e065a507142f48525935cbfd836588d"
    assert image.processed == True
    assert image.representations
    assert image.full == "https://derpicdn.net/img/view/2017/3/11/1384692.png"
    assert image.large == "https://derpicdn.net/img/2017/3/11/1384692/large.png"
    assert image.medium == "https://derpicdn.net/img/2017/3/11/1384692/medium.png"
    assert image.small == "https://derpicdn.net/img/2017/3/11/1384692/small.png"
    assert image.tall == "https://derpicdn.net/img/2017/3/11/1384692/tall.png"
    assert image.thumb == "https://derpicdn.net/img/2017/3/11/1384692/thumb.png"
    assert image.thumb_small == "https://derpicdn.net/img/2017/3/11/1384692/thumb_small.png"
    assert image.thumb_tiny == "https://derpicdn.net/img/2017/3/11/1384692/thumb_tiny.png"
    assert image.score == 1849
    assert image.sha512_hash == "a5b68e1cb435a818cc15d5a4e8f879d350700ae1dbe9d12b7d9e421abc6d2f6b622318d99d0e5b120c2c59b3df3b9b120e065a507142f48525935cbfd836588d"
    assert image.source_url == "http://yakovlev-vad.deviantart.com/art/Favorite-place-Color-Sketch-668408843"
    assert image.spoilered == False
    assert image.tag_count == 39
    assert image.thumbnails_generated == True
    assert image.updated_at == "2019-12-20T10:09:44"
    assert image.uploader == None
    assert image.uploader_id == None
    assert image.upvotes == 1855
    assert image.view_url == "https://derpicdn.net/img/view/2017/3/11/1384692__safe_artist-colon-yakovlev-dash-vad_fluttershy_pegasus_pony_-colon-3_bed_behaving+like+a+cat_box_cheek+fluff_chest+fluff_colored+sketch_cute_d.png"
    assert image.width == 1400
    assert image.wilson_score == 0.9911990843331066

    assert image.tag_ids
    assert 27724 in image.tag_ids

    assert image.tags
    assert "fluttershy" in image.tags

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
