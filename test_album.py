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


def test_rating_none():
    album = Album("Rabies", "Skinny Puppy")
    album.calc_rating()
    assert not album.rating
    album.add_track(Track("Rodent"))
    album.add_track(Track("Hexonxonx"))
    album.calc_rating()
    assert not album.rating


def test_rating():
    album = Album("Mind: The Perpetual Intercourse", "Skinny Puppy")
    album.add_track(Track("One Time One Place", 4))
    album.calc_rating()
    assert album.rating == 4.0
    album.add_track(Track("God's Gift (Maggot)", 4))
    album.add_track(Track("Three Blind Mice", 4))
    album.add_track(Track("Love", 5))
    album.add_track(Track("Stairs And Flowers", 4))
    album.add_track(Track("Antagonism", 3.5))
    album.add_track(Track("200 Years", 3))
    album.add_track(Track("Dig It", 4.5))
    album.add_track(Track("Burnt With Water", 3.5))
    album.add_track(Track("Chainsaw", 4))
    album.add_track(Track("Addiction", 4.5))
    album.add_track(Track("Stairs And Flowers (Dub)", 3.5))
    album.add_track(Track("Deep Down Trauma Hounds", 4))
    album.calc_rating()
    assert round(album.rating, 4) == 3.9615


def test_rating_mixed():
    album = Album("Mei-Jyu", "Alio Die + Jack Or Jive")
    album.add_track(Track("Meijyu", 3))
    # This track is missing a rating
    album.add_track(Track("Fluff Of A Dandelion"))
    album.add_track(Track("Make An Arc Through The Air", 3))
    album.calc_rating()
    assert round(album.rating, 4) == 3.0
