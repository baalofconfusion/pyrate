import re


class Track:
    def __init__(self, text, rating=None, artist=None):
        self.title = text
        self.rating = rating
        self.artist = artist

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

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        if not artist:
            self._artist = None
        else:
            self._artist = artist


def main():
    # track = Track("\t\t1. Destination")
    parse_line("****+\t\t1. Malign -- Skin & Lye")
    parse_line("\t\t1. Destination")
    # print(track)


def parse_line(line):
    if match := re.search(r"([\*\+]*)\t\t(\d+)\. (?:(?:(.*?)(?: -- )(.*))|(.*))", line):
        # group 2 is the track number which is not being used right now
        rating = calc_rating(match.group(1))
        title = match.group(4)
        if title == None:
            title = match.group(5)
        return Track(title, rating, match.group(3))
    return None


def calc_rating(text):
    val = text.count("*") + (text.count("+") * 0.5)
    if val < 0.5:
        return None
    else:
        return val


if __name__ == "__main__":
    main()
