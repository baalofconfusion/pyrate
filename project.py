from parserat import parse
from sortrat import sort_average
from dumprat import dump_ratings


def main():
    collection = load_collection("./test_files/Curve.txt")
    sort_collection(collection)
    write_collection(collection, "sorted.txt")


def load_collection(filename):
    return parse(filename)


def sort_collection(collection):
    sort_average(collection)


def write_collection(collection, filename):
    dump_ratings(collection, filename)


if __name__ == "__main__":
    main()
