import pytest
from track import Track


def test_bad():
    with pytest.raises(TypeError):
        Track()
    with pytest.raises(ValueError):
        Track("")
    with pytest.raises(ValueError):
        Track("The Dream", "Three")


def test_init():
    track = Track("Destination")
    assert track.title == "Destination"
    assert track.rating == None
    assert track.artist == None
    track = Track("The Hanging Garden", 4)
    assert track.title == "The Hanging Garden"
    assert track.rating == 4.0
    assert track.artist == None
    track = Track("Bad Medicine Waltz", 1.5)
    assert track.title == "Bad Medicine Waltz"
    assert track.rating == 1.5
    assert track.artist == None
