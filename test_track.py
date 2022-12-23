import pytest
from track import Track
from track import parse_line


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
    track = Track("The Hanging Garden", 4)
    assert track.title == "The Hanging Garden"
    assert track.rating == 4.0
    track = Track("Bad Medicine Waltz", 1.5)
    assert track.title == "Bad Medicine Waltz"
    assert track.rating == 1.5


def test_parse():
    assert parse_line("") == None
    track = parse_line("\t\t1. Destination")
    assert track.title == "Destination"
    assert track.rating == None
    track = parse_line("****+\t\t3. Iceblink Luck")
    assert track.title == "Iceblink Luck"
    assert track.rating == 4.5
