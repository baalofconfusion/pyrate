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
    track = Track("\t\t1. Destination")
    print(track)


if __name__ == "__main__":
    main()
