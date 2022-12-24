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
    assert track.artist == None
    track = Track("The Hanging Garden", 4)
    assert track.title == "The Hanging Garden"
    assert track.rating == 4.0
    assert track.artist == None
    track = Track("Bad Medicine Waltz", 1.5)
    assert track.title == "Bad Medicine Waltz"
    assert track.rating == 1.5
    assert track.artist == None


def test_parse_no_track():
    assert parse_line("") == None
    assert parse_line("Sisters Of Mercy") == None
    assert parse_line("\tFear Of A Blank Planet") == None


def test_parse():
    track = parse_line("\t\t1. Destination")
    assert track.title == "Destination"
    assert track.rating == None
    assert track.artist == None
    track = parse_line("****+\t\t3. Iceblink Luck")
    assert track.title == "Iceblink Luck"
    assert track.rating == 4.5
    assert track.artist == None
    # Verify that a leading "-" is handled
    track = parse_line("-\t\t1. Houston Landing 3.15.02")
    assert track.title == "Houston Landing 3.15.02"
    assert track.rating == None
    assert track.artist == None
    track = parse_line("***\t\t9. (Candlemas): / Cauldron Of Cerridwen")
    assert track.title == "(Candlemas): / Cauldron Of Cerridwen"
    assert track.rating == 3.0
    assert track.artist == None


def test_parse_artist():
    track = parse_line("****+\t\t1. Malign -- Skin & Lye")
    assert track.title == "Skin & Lye"
    assert track.rating == 4.5
    assert track.artist == "Malign"
    track = parse_line("\t\t2. Agathodaimon -- Tongue Of Thorns")
    assert track.title == "Tongue Of Thorns"
    assert track.rating == None
    assert track.artist == "Agathodaimon"
