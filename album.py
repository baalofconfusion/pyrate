class Album:
    def __init__(self, title, artist=None):
        self.track_list = []
        self.title = title
        self.artist = artist

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Album must have title")
        self._title = title

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        if not artist:
            artist = "Various Artists"
        self._artist = artist

    def add_track(self, track):
        if track:
            self.track_list.append(track)


def main():
    album = Album("Test Title")
    print(album)


if __name__ == "__main__":
    main()
