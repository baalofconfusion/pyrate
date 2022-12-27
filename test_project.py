from project import load_collection


def test_load_collection():
    albums = load_collection("./test_files/Curve.txt")
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
