from project import load_collection
from project import sort_collection


def test_load_collection():
    collection = load_collection("./test_files/Curve.txt")
    assert collection is not None
    assert len(collection) == 22
    album = collection[0]
    assert album.artist == "Curve"
    assert album.title == "Blindfold"
    track_list = album.track_list
    assert len(track_list) == 4
    track = track_list[1]
    assert track.title == "I Speak Your Every Word"
    assert track.rating == 4.0
    assert album.rating == 4.25
    album = collection[11]
    assert album.artist == "Curve"
    assert album.title == "Peel Session Sept 17, 1993"
    track_list = album.track_list
    assert len(track_list) == 1
    track = track_list[0]
    assert track.title == "Turkey Crossing"
    assert track.rating == 3.5


def test_sort():
    collection = load_collection("./test_files/MiniCollection.txt")
    assert collection is not None
    assert len(collection) == 12
    sort_collection(collection)
    album = collection[0]
    assert album.title == "Just For A Day"
    assert round(album.rating, 2) == 4.28
    album = collection[2]
    assert album.title == "Loveless"
    assert round(album.rating, 2) == 3.91
    album = collection[11]
    assert album.title == "Hollow Ways"
    assert album.rating == None
