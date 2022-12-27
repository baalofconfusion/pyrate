import pytest
from album import Album
from track import Track


def test_bad():
    with pytest.raises(TypeError):
        Album()
    with pytest.raises(ValueError):
        Album("")


def test_init():
    album = Album("Disease Of Lady Madeline, The")
    assert album.title == "Disease Of Lady Madeline, The"
    assert album.artist == "Various Artists"
    assert len(album.track_list) == 0
    assert not album.rating
    album = Album("In The Flat Field", "Bauhaus")
    assert album.artist == "Bauhaus"
    assert album.title == "In The Flat Field"
    assert len(album.track_list) == 0
    assert not album.rating


def test_add_track():
    album = Album("Swing The Heartache", "Bauhaus")
    album.add_track(Track("Silent Hedges"))
    album.add_track(Track("Third Uncle"))
    assert album.title == "Swing The Heartache"
    assert len(album.track_list) == 2
    assert not album.rating
    album.add_track(None)
    assert len(album.track_list) == 2
    assert not album.rating
