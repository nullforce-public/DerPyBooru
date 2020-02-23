from derpibooru import Search
from derpibooru.image import Image
from derpibooru.request import get_image_data

def test_get_image_data():
    """
    Tests getting image data for a given id
    """
    image = Image(get_image_data(1384692))

    assert image.data
    assert image.aspect_ratio == 0.7588075880758808
    assert image.comment_count >= 32
    assert image.created_at == "2017-03-11T20:32:14"
    assert image.deletion_reason == None
    assert image.description == "Pony in box, inspired by my cat as usual X3 Just quick color sketch)"
    assert image.downvotes == image.upvotes - image.score
    assert image.duplicate_of == None
    assert image.faves >= 0
    assert image.first_seen_at == "2017-03-11T20:32:14"
    assert image.format == "PNG"
    assert image.height == 1845
    assert image.hidden_from_users == False
    assert image.id == 1384692
    assert image.intensities
    assert image.intensities["ne"] >= 0
    assert image.intensities["nw"] >= 0
    assert image.intensities["se"] >= 0
    assert image.intensities["sw"] >= 0
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
    assert image.score == image.upvotes - image.downvotes
    assert image.sha512_hash == "a5b68e1cb435a818cc15d5a4e8f879d350700ae1dbe9d12b7d9e421abc6d2f6b622318d99d0e5b120c2c59b3df3b9b120e065a507142f48525935cbfd836588d"
    assert image.source_url == "http://yakovlev-vad.deviantart.com/art/Favorite-place-Color-Sketch-668408843"
    assert image.spoilered == False
    assert image.tag_count >= 0
    assert image.tag_ids
    assert image.tags
    assert image.thumbnails_generated == True
    assert image.updated_at == "2019-12-20T10:09:44"
    assert image.uploader == None
    assert image.uploader_id == None
    assert image.upvotes == image.score + image.downvotes
    assert image.view_url == "https://derpicdn.net/img/view/2017/3/11/1384692__safe_artist-colon-yakovlev-dash-vad_fluttershy_pegasus_pony_-colon-3_bed_behaving+like+a+cat_box_cheek+fluff_chest+fluff_colored+sketch_cute_d.png"
    assert image.width == 1400
    assert image.wilson_score >= 0

def test_query():
    """
    Tests whether the results in a query contain the tag that was being searched
    for
    """
    limit, tag = 10, "sunset shimmer"
    images = [image for image in Search().query(tag).limit(limit)]

    assert len(images) == limit

    for image in images:
        assert tag in image.tags

def test_ascending():
    """
    Tests whether ascending search is in the correct order
    """
    limit = 10
    images = [image for image in Search().ascending().limit(limit)]

    assert len(images) == limit

    for image in images:
        # Check if the images are in ascending order
        # by comparing the ID of the next image 
        if image is not images[-1]:
            next_image = images[images.index(image) + 1]
            assert image.id < next_image.id

def test_descending():
    """
    Tests whether descending search is in the correct order
    """
    limit = 10
    images = [image for image in Search().descending().limit(limit)]

    assert len(images) == limit

    for image in images:
        # Check if the image IDs are listed in descending order
        # by comparing the ID of the next image
        if image is not images[-1]:
            next_image = images[images.index(image) + 1]
            assert image.id > next_image.id
