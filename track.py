import re


class Track:
    def __init__(self, text, rating=None):
        self.title = text
        self.rating = rating

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("A track must have a title")
        self._title = title

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if not rating:
            self._rating = None
        else:
            self._rating = float(rating)


def main():
    track = Track("\t\t1. Destination")
    print(track)


def parse_line(line):
    if match := re.search(r"([\*\+]*)\t\t(\d+)\. (.*)", line):
        # group 2 if the track number which is not being used right now
        rating = calc_rating(match.group(1))
        return Track(match.group(3), rating)
    return None


def calc_rating(text):
    val = text.count("*") + (text.count("+") * 0.5)
    if val < 0.5:
        return None
    else:
        return val


if __name__ == "__main__":
    main()
