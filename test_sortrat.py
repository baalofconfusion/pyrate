from sortrat import sort_average
from album import Album


def test_empty():
    collection = sort_average([])
    assert collection is not None
    assert len(collection) == 0


def test_sort():
    collection = []
    album = Album("The Sky Moves Sideways", "Porcupine Tree")
    # For testing, just set the rating directly
    album._rating = 4.2
    collection.append(album)
    collection = sort_average(collection)
    assert collection is not None
    assert len(collection) == 1
    album = Album("Succour")
    album._rating = 2.36
    collection.append(album)
    album = Album("Any Day Now", "Legendary Pink Dots")
    album._rating = 4.19
    collection.append(album)
    # Note that the current code uses in-place sorting
    sort_average(collection)
    assert len(collection) == 3
    a = collection[0]
    assert a.title == "The Sky Moves Sideways"
    a = collection[1]
    assert a.title == "Any Day Now"
    a = collection[2]
    assert a.title == "Succour"


def test_none():
    collection = []
    album = Album("The Sky Moves Sideways", "Porcupine Tree")
    album._rating = 4.2
    collection.append(album)
    album = Album("Mindstrip", "Suicide Commando")
    collection.append(album)
    album = Album("Different Stars", "Trespassers William")
    album._rating = 4.336
    collection.append(album)
    sort_average(collection)
    assert len(collection) == 3
    a = collection[0]
    assert a.title == "Different Stars"
    a = collection[1]
    assert a.title == "The Sky Moves Sideways"
    a = collection[2]
    assert a.title == "Mindstrip"
