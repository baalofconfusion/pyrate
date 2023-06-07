import json


def dump_ratings(collection, filename):
    with open(filename, "w") as file:
        for album in collection:
            if album.rating:
                file.write(f"{album.rating:.4f}  {album.title}  by:  {album.artist}\n")


def dump_jason(collection, filename):
    with open(filename, "w") as file:
        file.write(json.dumps(collection))
