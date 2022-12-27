import pytest

from parserat import parse
from parserat import parse_line


def test_bad_file():
    with pytest.raises(FileNotFoundError):
        parse("badfile.txt")


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


def test_single_artist():
    albums = parse("./test_files/Tribe.txt")
    assert albums is not None
    assert len(albums) == 1
    album = albums[0]
    assert album.artist == "Tribe"
    assert album.title == "Abort"
    track_list = album.track_list
    assert len(track_list) == 12
    track = track_list[4]
    assert track.title == "Joyride (I Saw The Film)"
    assert track.rating == 5.0


def test_multiple_album():
    albums = parse("./test_files/Curve.txt")
    assert albums is not None
    assert len(albums) == 22
    album = albums[0]
    assert album.artist == "Curve"
    assert album.title == "Blindfold"
    track_list = album.track_list
    assert len(track_list) == 4
    track = track_list[1]
    assert track.title == "I Speak Your Every Word"
    assert track.rating == 4.0
    assert album.rating == 4.25
    album = albums[11]
    assert album.artist == "Curve"
    assert album.title == "Peel Session Sept 17, 1993"
    track_list = album.track_list
    assert len(track_list) == 1
    track = track_list[0]
    assert track.title == "Turkey Crossing"
    assert track.rating == 3.5


def test_comp():
    albums = parse("./test_files/GothicRock.txt")
    assert albums is not None
    assert len(albums) == 1
    album = albums[0]
    assert album.artist == "Various Artists"
    assert album.title == "Gothic Rock"
    assert round(album.rating, 4) == 3.7105
