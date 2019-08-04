# -*- coding: utf-8 -*-

# Copyright (c) 2019, Nullforce
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Represents the image JSON object returned from ther derpibooru API"""

from re import sub
import sys
import dateutil.parser
from .request import get_image_data

__all__ = [
    "Representations",
    "Image"
]

if sys.version_info[0] >= 3:
    unicode = str

def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False

def from_str(x):
    assert isinstance(x, (str, unicode))
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x):
    return dateutil.parser.parse(x)


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x):
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x):
    assert isinstance(x, bool)
    return x


def to_float(x):
    assert isinstance(x, float)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()

def prepend_https(partial_uri):
    return f"https:{partial_uri}"

class Representations:
    def __init__(self, thumb_tiny, thumb_small, thumb, small, medium, large, tall, full):
        self.thumb_tiny = prepend_https(thumb_tiny)
        self.thumb_small = prepend_https(thumb_small)
        self.thumb = prepend_https(thumb)
        self.small = prepend_https(small)
        self.medium = prepend_https(medium)
        self.large = prepend_https(large)
        self.tall = prepend_https(tall)
        self.full = prepend_https(full)

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        thumb_tiny = from_union([from_str, from_none], obj.get(u"thumb_tiny"))
        thumb_small = from_union([from_str, from_none], obj.get(u"thumb_small"))
        thumb = from_union([from_str, from_none], obj.get(u"thumb"))
        small = from_union([from_str, from_none], obj.get(u"small"))
        medium = from_union([from_str, from_none], obj.get(u"medium"))
        large = from_union([from_str, from_none], obj.get(u"large"))
        tall = from_union([from_str, from_none], obj.get(u"tall"))
        full = from_union([from_str, from_none], obj.get(u"full"))
        return Representations(thumb_tiny, thumb_small, thumb, small, medium, large, tall, full)

    def to_dict(self):
        result = {}
        result[u"thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        result[u"thumb_small"] = from_union([from_str, from_none], self.thumb_small)
        result[u"thumb"] = from_union([from_str, from_none], self.thumb)
        result[u"small"] = from_union([from_str, from_none], self.small)
        result[u"medium"] = from_union([from_str, from_none], self.medium)
        result[u"large"] = from_union([from_str, from_none], self.large)
        result[u"tall"] = from_union([from_str, from_none], self.tall)
        result[u"full"] = from_union([from_str, from_none], self.full)
        return result


class Image:
    def __init__(self, id, created_at, updated_at, first_seen_at, tags, tag_ids, uploader_id, score, comment_count, width, height, tag_count, file_name, description, uploader, image, upvotes, downvotes, faves, aspect_ratio, original_format, mime_type, sha512_hash, orig_sha512_hash, source_url, representations, is_rendered, is_optimized, interactions, spoilered):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.first_seen_at = first_seen_at
        self.tags = tags
        self.tag_ids = tag_ids
        self.uploader_id = uploader_id
        self.score = score
        self.comment_count = comment_count
        self.width = width
        self.height = height
        self.tag_count = tag_count
        self.file_name = file_name
        self.description = description
        self.uploader = uploader
        self.image = prepend_https(image)
        self.image2 = prepend_https(image)
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.faves = faves
        self.aspect_ratio = aspect_ratio
        self.original_format = original_format
        self.mime_type = mime_type
        self.sha512_hash = sha512_hash
        self.orig_sha512_hash = orig_sha512_hash
        self.source_url = source_url
        self.representations = representations
        self.is_rendered = is_rendered
        self.is_optimized = is_optimized
        self.interactions = interactions
        self.spoilered = spoilered

        self._data = self.to_dict()

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get(u"id"))
        created_at = from_union([from_datetime, from_none], obj.get(u"created_at"))
        updated_at = from_union([from_datetime, from_none], obj.get(u"updated_at"))
        first_seen_at = from_union([from_datetime, from_none], obj.get(u"first_seen_at"))
        tags_temp = from_union([from_str, from_none], obj.get(u"tags"))
        if isinstance(tags_temp, (str, unicode)):
            tags = str(tags_temp).split(", ")
        tag_ids = from_union([lambda x: from_list(from_int, x), from_none], obj.get(u"tag_ids"))
        uploader_id = from_union([from_int, from_none], obj.get(u"uploader_id"))
        score = from_union([from_int, from_none], obj.get(u"score"))
        comment_count = from_union([from_int, from_none], obj.get(u"comment_count"))
        width = from_union([from_int, from_none], obj.get(u"width"))
        height = from_union([from_int, from_none], obj.get(u"height"))
        tag_count = from_union([from_int, from_none], obj.get(u"tag_count"))
        file_name = from_union([from_str, from_none], obj.get(u"file_name"))
        description = from_union([from_str, from_none], obj.get(u"description"))
        uploader = from_union([from_str, from_none], obj.get(u"uploader"))
        image = from_union([from_str, from_none], obj.get(u"image"))
        upvotes = from_union([from_int, from_none], obj.get(u"upvotes"))
        downvotes = from_union([from_int, from_none], obj.get(u"downvotes"))
        faves = from_union([from_int, from_none], obj.get(u"faves"))
        aspect_ratio = from_union([from_float, from_none], obj.get(u"aspect_ratio"))
        original_format = from_union([from_str, from_none], obj.get(u"original_format"))
        mime_type = from_union([from_str, from_none], obj.get(u"mime_type"))
        sha512_hash = from_union([from_str, from_none], obj.get(u"sha512_hash"))
        orig_sha512_hash = from_union([from_str, from_none], obj.get(u"orig_sha512_hash"))
        source_url = from_union([from_str, from_none], obj.get(u"source_url"))
        representations = from_union([Representations.from_dict, from_none], obj.get(u"representations"))
        is_rendered = from_union([from_bool, from_none], obj.get(u"is_rendered"))
        is_optimized = from_union([from_bool, from_none], obj.get(u"is_optimized"))
        interactions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get(u"interactions"))
        spoilered = from_union([from_bool, from_none], obj.get(u"spoilered"))
        return Image(id, created_at, updated_at, first_seen_at, tags, tag_ids, uploader_id, score, comment_count, width, height, tag_count, file_name, description, uploader, image, upvotes, downvotes, faves, aspect_ratio, original_format, mime_type, sha512_hash, orig_sha512_hash, source_url, representations, is_rendered, is_optimized, interactions, spoilered)

    def to_dict(self):
        separator = ", "
        result = {}
        result[u"id"] = from_union([from_int, from_none], self.id)
        result[u"created_at"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        result[u"updated_at"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        result[u"first_seen_at"] = from_union([lambda x: x.isoformat(), from_none], self.first_seen_at)
        result[u"tags"] = from_union([from_str, from_none], separator.join(self.tags))
        result[u"tag_ids"] = from_union([lambda x: from_list(from_int, x), from_none], self.tag_ids)
        result[u"uploader_id"] = from_union([from_int, from_none], self.uploader_id)
        result[u"score"] = from_union([from_int, from_none], self.score)
        result[u"comment_count"] = from_union([from_int, from_none], self.comment_count)
        result[u"width"] = from_union([from_int, from_none], self.width)
        result[u"height"] = from_union([from_int, from_none], self.height)
        result[u"tag_count"] = from_union([from_int, from_none], self.tag_count)
        result[u"file_name"] = from_union([from_str, from_none], self.file_name)
        result[u"description"] = from_union([from_str, from_none], self.description)
        result[u"uploader"] = from_union([from_str, from_none], self.uploader)
        result[u"image"] = from_union([from_str, from_none], self.image)
        result[u"upvotes"] = from_union([from_int, from_none], self.upvotes)
        result[u"downvotes"] = from_union([from_int, from_none], self.downvotes)
        result[u"faves"] = from_union([from_int, from_none], self.faves)
        result[u"aspect_ratio"] = from_union([to_float, from_none], self.aspect_ratio)
        result[u"original_format"] = from_union([from_str, from_none], self.original_format)
        result[u"mime_type"] = from_union([from_str, from_none], self.mime_type)
        result[u"sha512_hash"] = from_union([from_str, from_none], self.sha512_hash)
        result[u"orig_sha512_hash"] = from_union([from_str, from_none], self.orig_sha512_hash)
        result[u"source_url"] = from_union([from_str, from_none], self.source_url)
        result[u"representations"] = from_union([lambda x: to_class(Representations, x), from_none], self.representations)
        result[u"is_rendered"] = from_union([from_bool, from_none], self.is_rendered)
        result[u"is_optimized"] = from_union([from_bool, from_none], self.is_optimized)
        result[u"interactions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.interactions)
        result[u"spoilered"] = from_union([from_bool, from_none], self.spoilered)
        return result

    # backwards compat
    @property
    def comments(self):
        return []

    @property
    def data(self):
        return self._data

    @property
    def faved_by(self):
        return []

    @property
    def full(self):
        full = self.representations.full
        url = sub("_.*\.", ".", full)
        return url

    @property
    def large(self):
        return self.representations.large

    @property
    def medium(self):
        return self.representations.medium

    @property
    def small(self):
        return self.representations.small

    @property
    def tall(self):
        return self.representations.tall

    @property
    def thumb(self):
        return self.representations.thumb

    @property
    def thumb_tiny(self):
        return self.representations.thumb_tiny

    @property
    def thumb_small(self):
        return self.representations.thumb_small

    @property
    def url(self):
        return f"https://derpibooru.org/{self.id}"

    def update(self):
        data = get_image_data(self.id)

        if data:
            self._data = data

def image_from_dict(s):
    return Image.from_dict(s)

def image_to_dict(x):
    return to_class(Image, x)
