import pytest

from parserat import parse


def test_bad():
    with pytest.raises(FileNotFoundError):
        parse("badfile.txt")


def test_single():
    albums = parse("./test_files/Tribe.txt")
    assert albums is not None
    assert len(albums) == 1
    album = albums(0)
    assert album.artist == "Tribe"
    assert album.title == "Abort"
    track_list = album.track_list
    assert len(track_list) == 12
    track = track_list(4)
    assert track.title == "Joyride (I Saw The Film)"
    assert track.rating == 5.0
