from parserat import parse
from sortrat import sort_average


def main():
    collection = load_collection("./test_files/Curve.txt")
    sort_collection(collection)


def load_collection(filename):
    return parse(filename)


def sort_collection(collection):
    sort_average(collection)


def function_n():
    ...


if __name__ == "__main__":
    main()
