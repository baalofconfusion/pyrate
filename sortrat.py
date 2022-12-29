from operator import attrgetter


def sort_average(collection):
    collection.sort(key=attrgetter("sort_rating"), reverse=True)
    # Return the sorted collection for convenience
    return collection


def main():
    ...


if __name__ == "__main__":
    main()
