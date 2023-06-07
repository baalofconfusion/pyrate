from project import load_collection
from project import sort_collection
from project import write_collection


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


def test_sort_collection():
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


def test_write_collection():
    collection = load_collection("./test_files/MiniCollection.txt")
    write_collection(collection, "mini_unsorted.txt")
    sort_collection(collection)
    write_collection(collection, "mini_sorted.txt")
    line_number = 0
    with open("mini_unsorted.txt") as file:
        for line in file:
            if line_number == 0:
                assert "All Virgos Are Mad" in line
            elif line_number == 1:
                assert "Within The Realm" in line
            elif line_number == 2:
                assert "Into The Labyrinth" in line
            else:
                break
            line_number += 1
    with open("mini_sorted.txt") as file:
        for line in file:
            if line_number == 0:
                assert "Just For A Day" in line
            elif line_number == 1:
                assert "Within The Realm" in line
            elif line_number == 2:
                assert "Loveless" in line
            else:
                break
            line_number += 1
